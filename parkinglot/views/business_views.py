# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models import *
from django.utils import timezone
from django.db import transaction


@transaction.commit_on_success
def order_lot(request):
    if request.method == 'POST':
        if request.session.get('login_user', False):
            Order.remove_invalid_orders()
            username = request.POST['username']
            parkinglot_id = request.POST['parkinglot_id']
            try:
                user = User.objects.get(username=username)
                parkinglot = Parkinglot.objects.get(id=parkinglot_id)
                the_lot = parkinglot.get_unused_lot()
                if user.have_unfinished_order(parkinglot):
                    # transaction.commit()
                    return render(request, 'parkinglot/error_info.html', {'user': user, 'error_info': '存在未完成订单，请勿重复预定！'})
                if the_lot is None:
                    # transaction.commit()
                    return render(request, 'parkinglot/error_info.html', {'user': user, 'error_info': '停车场已满！'})
                try:
                    order = Order(
                        user=user, parkinglot=parkinglot, lot=the_lot, order_time=timezone.now(), start_time=None,
                        end_time=None)
                    the_lot.status = 1
                    the_lot.save()
                    order.save()
                except:
                    # transaction.rollback()
                    return render(request, 'parkinglot/error_info.html', {'user': user, 'error_info': '预定失败！'})
                else:
                    # transaction.commit()
                    return HttpResponseRedirect(reverse('user_order', args=(1,)))
            except User.DoesNotExist, Parkinglot.DoesNotExist:
                # transaction.commit()
                return render(request, 'parkinglot/error_info.html', {'user': user, 'error_info': '预定失败！'})
        else:
            # transaction.commit()
            return HttpResponseRedirect(reverse('login'))
