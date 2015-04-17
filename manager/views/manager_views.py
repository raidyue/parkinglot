# encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from parkinglot.models import *
from django.utils import timezone
from django.db import transaction
import math


def index(request):
    if request.session.get('login_manager', False):
        name = request.session['login_manager']
        manager = Manager.objects.get(name=name)
        parkinglot = manager.parkinglot
        return render(request, 'manager/manager_index.html', {'manager': manager, 'parkinglot': parkinglot})
    return HttpResponseRedirect(reverse('manager_login'))


def login(request):
    if request.method == 'GET':
        manager_login_info = None
        if request.session.get('manager_login_info', False):
            manager_login_info = request.session.pop('manager_login_info')
        return render(request, 'manager/manager_login.html', {'manager_login_info': manager_login_info})
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            manager = Manager.objects.get(name=name)
            if manager.password == password:
                request.session['login_manager'] = manager.name
                return HttpResponseRedirect(reverse('manager_index'))
            else:
                request.session['manager_login_info'] = '密码错误'
                request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('manager_login'))
        except Manager.DoesNotExist:
            request.session['manager_login_info'] = '该管理员不存在'
            return HttpResponseRedirect(reverse('manager_login'))


def logout(request):
    if request.session.get('login_manager', False):
        del request.session['login_manager']
        return HttpResponseRedirect(reverse('manager_index'))
    return HttpResponseRedirect(reverse('manager_index'))


def order(request, status, page_id):
    if request.session.get('login_manager', False):
        if request.method == 'GET':
            name = request.session['login_manager']
            manager = Manager.objects.get(name=name)
            status = int(status)
            orders = Order.objects.filter(parkinglot=manager.parkinglot).order_by('-order_time')
            page_num = 12
            page_count = int(math.ceil(len(orders) / float(page_num)))
            page_id = int(page_id)
            if len(orders) < ((page_id - 1) * page_num):
                return HttpResponseRedirect(reverse('user_order', args=(1,)))
            # 0=ordering 1=parking 2=finished 3=aborted 4=all
            if status == 0:
                orders = [order for order in orders if order.is_valid() and order.status == 0]
                page_count = int(math.ceil(len(orders) / float(page_num)))
                orders = orders[((page_id - 1) * page_num): (page_id * page_num)]
                return render(request, 'manager/manager_order_ordering.html',
                              {'manager': manager, 'orders': orders, 'status': status, 'page_count': page_count,
                               'page_id': page_id})
            elif status == 1:
                orders = [order for order in orders if order.status == 1]
                page_count = int(math.ceil(len(orders) / float(page_num)))
                orders = orders[((page_id - 1) * page_num): (page_id * page_num)]
                return render(request, 'manager/manager_order_parking.html',
                              {'manager': manager, 'orders': orders, 'status': status, 'page_count': page_count,
                               'page_id': page_id})
            elif status == 2:
                orders = [order for order in orders if order.status == 2]
                page_count = int(math.ceil(len(orders) / float(page_num)))
                orders = orders[((page_id - 1) * page_num): (page_id * page_num)]
                return render(request, 'manager/manager_order_finished.html',
                              {'manager': manager, 'orders': orders, 'status': status, 'page_count': page_count,
                               'page_id': page_id})
            elif status == 3:
                orders = [order for order in orders if not order.is_valid() and order.status == 0]
                page_count = int(math.ceil(len(orders) / float(page_num)))
                orders = orders[((page_id - 1) * page_num): (page_id * page_num)]
                return render(request, 'manager/manager_order_aborted.html',
                              {'manager': manager, 'orders': orders, 'status': status, 'page_count': page_count,
                               'page_id': page_id})
            elif status == 4:
                orders = orders[((page_id - 1) * page_num): (page_id * page_num)]
                for order in orders:
                    if order.status == 0 and not order.is_valid():
                        order.status = 4
                return render(request, 'manager/manager_order.html',
                              {'manager': manager, 'orders': orders, 'status': status, 'page_count': page_count,
                               'page_id': page_id})
            else:
                return Http404
    return HttpResponseRedirect(reverse('manager_login'))


def confirm_order(request):
    if request.method == 'POST':
        if request.session.get('login_manager', False):
            order_id = request.POST['order_id']
            status = request.POST['status']
            try:
                order = Order.objects.get(id=order_id)
                if order.status != 0:
                    pass
                order.status = 1
                order.start_time = timezone.now()
                order.save()
                return HttpResponseRedirect(reverse('manager_order', args=(1, 1)))
            except Order.DoesNotExist:
                pass


@transaction.commit_manually
def parking_leave(request):
    if request.method == 'POST':
        if request.session.get('login_manager', False):
            order_id = request.POST['order_id']
            status = request.POST['status']
            manager = Manager.objects.get(name=request.session['login_manager'])
            try:
                order = Order.objects.get(id=order_id)
                lot = order.lot
                lot.status = 0
                if order.status != 1:
                    transaction.commit()
                    return HttpResponse('订单状态错误！')
                order.status = 2
                order.end_time = timezone.now()
                try:
                    order.save()
                    lot.save()
                except:
                    transaction.rollback()
                    return HttpResponseRedirect('parking_leave failed!')
                else:
                    retval = render_to_response('manager/completed_order_info.html',
                                                {'order': order, 'manager': manager},
                                                context_instance=RequestContext(request))
                    transaction.commit()
                    return retval
            except Exception, e:
                transaction.rollback()
                print type(e)
                return HttpResponse("leave failed!")




