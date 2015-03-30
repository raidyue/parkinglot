# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from parkinglot.models import *
from django.utils import timezone


def parkinglot_info(request):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])

        if request.method == 'GET':
            return render(request, 'manager/manager_parkinglot.html', {'manager': manager})


def parkinglot_update(request):
    if request.session.get('login_manager', False):
        manager = Manager.objects.get(name=request.session['login_manager'])
        if request.method == 'GET':
            return render(request, 'manager/parkinglot_update.html', {'manager': manager})
        elif request.method == 'POST':
            pass
