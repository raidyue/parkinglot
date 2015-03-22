# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models import *
from django.utils import timezone
from django.db import transaction


def index(request):
    return render(request, 'manager/manager_index.html', {})


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
                request.session['manager_user'] = manager.name
                return HttpResponseRedirect(reverse('manager_index'))
            else:
                request.session['manager_login_info'] = '密码错误'
                request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('manager_login'))
        except Manager.DoesNotExist:
            request.session['manager_login_info'] = '该管理员不存在'
            return HttpResponseRedirect(reverse('manager_login'))


def logout(request):
    if request.session.get('manager_user', False):
        del request.session['manager_user']
        return HttpResponseRedirect(reverse('manager_index'))
    return HttpResponseRedirect(reverse('manager_index'))
