# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models import *
from django.utils import timezone
from django.db import transaction


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


def order(request, status):
    if request.session.get('login_manager', False):
        if request.method == 'GET':
            name = request.session['login_manager']
            manager = Manager.objects.get(name=name)
            status = int(status)
            orders = []
            # 0=ordering 1=parking 2=finished 3=aborted 4=all
            if status == 0:
                orders = Consumption.objects.filter(status=0, parkinglot=manager.parkinglot)
                return render(request, 'manager/manager_order_ordering.html', {'manager': manager, 'orders': orders, 'status': status})
            elif status == 1:
                orders = Consumption.objects.filter(status=1, parkinglot=manager.parkinglot)
                return render(request, 'manager/manager_order_parking.html', {'manager': manager, 'orders': orders, 'status': status})
            elif status == 2:
                orders = Consumption.objects.filter(status=2, parkinglot=manager.parkinglot)
                return render(request, 'manager/manager_order_finished.html', {'manager': manager, 'orders': orders, 'status': status})
            elif status == 3:
                orders = Consumption.objects.filter(status=3, parkinglot=manager.parkinglot)
                return render(request, 'manager/manager_order_aborted.html', {'manager': manager, 'orders': orders, 'status': status})
            elif status == 4:
                orders = Consumption.objects.filter(parkinglot=manager.parkinglot)
                return render(request, 'manager/manager_order.html', {'manager': manager, 'orders': orders, 'status': status})
            print type(status)
            return render(request, 'manager/manager_order.html', {'manager': manager, 'orders': orders, 'status': status})
        return HttpResponseRedirect(reverse('manager_login'))


def confirm_order(request):
    if request.method == 'POST':
        if request.session.get('login_manager', False):
            order_id = request.POST['order_id']
            status = request.POST['status']
            try:
                order = Consumption.objects.get(id=order_id)
                if order.status != 0:
                    pass
                order.status = 1
                order.start_time = timezone.now()
                order.save()
                return HttpResponseRedirect(reverse('manager_order', args=(1,)))
            except Consumption.DoesNotExist:
                pass
