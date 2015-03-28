# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from parkinglot.models import *
from django.utils import timezone


def parkinglot_info(request):
    return render(request, 'manager/manager_parkinglot.html', {})