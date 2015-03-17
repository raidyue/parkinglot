# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *


def index(request):
    if request.session.get('username', False):
        username = request.session['username']
        user = User.objects.get(username=username)
        return render(request, 'parkinglot/index.html', {'user': user})
    return render(request, 'parkinglot/index.html', {})


def register(request):
    if request.method == 'GET':
        info = None
        if request.session.get('info', False):
            info = request.session.pop('info')
        return render(request, 'parkinglot/register.html', {'info': info})
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']
        if password != repeatPassword:
            request.session['info'] = '密码不一致'
            return HttpResponseRedirect(reverse('register'))
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username, password=password, email=email)
            user.save()
            request.session['user'] = user
            return HttpResponse(username + '-' + password + '-' + email)
        request.session['info'] = '用户已存在'
        return HttpResponseRedirect(reverse('index'))


def login(request):
    if request.method == 'GET':
        login_info = None
        if request.session.get('login_info', False):
            login_info = request.session.pop('login_info')
        return render(request, 'parkinglot/login.html', {'login_info': login_info})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = user.username
                return HttpResponseRedirect(reverse('index'))
            else:
                request.session['login_info'] = 'wrong password'
                return HttpResponseRedirect(reverse('login'))
        except User.DoesNotExist:
            request.session['login_info'] = '用户不存在'
            return HttpResponseRedirect(reverse('login'))


def logout(request):
    if request.session.get('user', False):
        del request.session['user']
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))
