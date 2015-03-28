# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models import *


def index(request):
    parkinglots = Parkinglot.objects.all()
    if request.session.get('login_user', False):
        username = request.session['login_user']
        print username
        user = User.objects.get(username=username)
        return render(request, 'parkinglot/index.html', {'user': user, 'parkinglots': parkinglots})
    return render(request, 'parkinglot/index.html', {'user': None, 'parkinglots': parkinglots})


def user(request):
    if request.session.get('login_user', False):
        username = request.session['login_user']
        user = User.objects.get(username=username)
        orders = Order.objects.filter(user=user)
        return render(request, 'parkinglot/user_order.html', {'orders': orders, 'user': user})
    return HttpResponseRedirect(reverse('login'))


def user_info(request):
    if request.session.get('login_user', False):
        username = request.session['login_user']
        user = User.objects.get(username=username)
        return render(request, 'parkinglot/user_info.html', {'user': user})
    return HttpResponseRedirect(reverse('login'))


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
        repeat_password = request.POST['repeatPassword']
        if password != repeat_password:
            request.session['info'] = '密码不一致'
            request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('register'))
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username, password=password, email=email)
            user.save()
            request.session['login_user'] = user.username
            request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('index'))
        request.session['info'] = '用户已存在'
        return HttpResponseRedirect(reverse('register'))


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
                request.session['login_user'] = user.username
                return HttpResponseRedirect(reverse('index'))
            else:
                request.session['login_info'] = 'wrong password'
                request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('login'))
        except User.DoesNotExist:
            request.session['login_info'] = '用户不存在'
            return HttpResponseRedirect(reverse('login'))


def logout(request):
    if request.session.get('login_user', False):
        del request.session['login_user']
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))
