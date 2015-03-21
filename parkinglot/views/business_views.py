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
                if the_lot is None:
                    return HttpResponse("failed!")
                try:
                    consumption = Consumption(
                        user=user, parkinglot=parkinglot, lot=the_lot, order_time=timezone.now(), start_time=None, end_time=None)
                    consumption.save()
                    if the_lot.status != 0:
                        raise RuntimeError
                    the_lot.status = 1
                    the_lot.save()
                except:
                    transaction.rollback()
                    return HttpResponse('commit failed!')
                else:
                    transaction.commit()
                return HttpResponse(consumption.id)
            except User.DoesNotExist, Parkinglot.DoesNotExist:
                return HttpResponse("failed")
        else:
            return HttpResponseRedirect(reverse('login'))
