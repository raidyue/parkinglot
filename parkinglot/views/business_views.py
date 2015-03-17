# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models import *
from django.utils import timezone
from django.db import transaction


@transaction.commit_manually
def order_lot(request):
    if request.method == 'POST':
        if request.session.get('login_user', False):
            username = request.POST['username']
            parkinglot_id = request.POST['parkinglot_id']
            try:
                user = User.objects.get(username=username)
                parkinglot = Parkinglot.objects.get(id=parkinglot_id)
                the_lot = parkinglot.get_unused_lot()
                try:
                    consumption = Consumption(
                        user=user, parkinglot=parkinglot, lot=the_lot, order_time=timezone.now())
                except:
                    transaction.rollback()
                else:
                    transaction.commit()
                    return HttpResponse(consumption.id + '-' + consumption.parkinglot.id + '-' + consumption.user.id)
            except User.DoesNotExist, Parkinglot.DoesNotExist:
                pass
        else:
            return HttpResponseRedirect(reverse('login'))
