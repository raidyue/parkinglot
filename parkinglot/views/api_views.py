from django.shortcuts import render
from django.http import HttpResponse
from ..utils import *
import json
from ..models import *
import pickle
# Create your views here.


def index(request, username):
    user = User.objects.get(username=username)
    data = {'username':user.username,'password':user.password,'over':user.over}
    return HttpResponse(json.dumps(response_result(code=400, msg='wrong param', data=data)))
