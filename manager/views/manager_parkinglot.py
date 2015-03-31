# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from parkinglot.models import *
from django.utils import timezone
import math


def parkinglot_info(request):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])

        if request.method == 'GET':
            return render(request, 'manager/manager_parkinglot.html', {'manager': manager})
    else:
        return HttpResponseRedirect(reverse('manager_login'))


def parkinglot_update(request):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])
        if request.method == 'GET':
            return render(request, 'manager/parkinglot_update.html', {'manager': manager})
        elif request.method == 'POST':
            name = request.POST['name']
            city = request.POST['city']
            address = request.POST['address']
            charge = request.POST['charge']
            try:
                charge = float(charge)
            except:
                return HttpResponseRedirect(reverse('manager_parkinglot'))
            parkinglot = manager.parkinglot
            if Parkinglot.is_parkinglot_not_exist(name) or name == parkinglot.name:
                parkinglot.name = name
                parkinglot.city = city
                parkinglot.address = address
                parkinglot.charge = charge
                parkinglot.save()
                return HttpResponseRedirect(reverse('manager_parkinglot'))
            else:
                return HttpResponseRedirect(reverse('parkinglot_update'))
    else:
        return HttpResponseRedirect(reverse('manager_login'))


def lot_update(request, page_id):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])
        parkinglot = manager.parkinglot
        all_lot = Lot.objects.filter(parkinglot=parkinglot)
        page_num = 12
        page_count = int(math.ceil(len(all_lot) / float(page_num)))
        page_id = int(page_id)
        if len(all_lot) < ((page_id - 1) * page_num):
            return HttpResponseRedirect(reverse('manager_lot', args=(1,)))
        all_lot = all_lot[((page_id - 1) * page_num): (page_id * page_num)]
        if request.method == 'POST':
            num = request.POST['num']
            if Lot.is_lot_exist(num):
                return render(request, 'manager/manager_lot.html',
                              {'manager': manager, 'all_lot': all_lot, 'info': '该车位已存在', 'page_id': page_id,
                               'page_count': page_count})
            lot = Lot(parkinglot=parkinglot, num=num)
            lot.save()
            return HttpResponseRedirect(reverse('manager_lot', args=(1,)))
        else:

            return render(request, 'manager/manager_lot.html',
                          {'manager': manager, 'all_lot': all_lot, 'page_id': page_id, 'page_count': page_count})
    else:
        return HttpResponseRedirect(reverse('manager_login'))


def lot_remove(request):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])
        parkinglot = manager.parkinglot
        if request.method == 'POST':
            lot_id = request.POST['lot_id']
            lot = Lot.objects.get(id=lot_id)
            if lot.status != 0:
                return HttpResponseRedirect(reverse('manager_lot', args=(1,)))
            lot.delete()
            return HttpResponseRedirect(reverse('manager_lot', args=(1,)))
    else:
        return HttpResponseRedirect(reverse('manager_login'))