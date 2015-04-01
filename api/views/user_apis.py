# encoding=utf-8
from django.http import HttpResponse
from ..utils import *
from parkinglot.models import *
# Create your views here.

# 根据用户名获取用户信息 GET
# 参数:
# username 用户名
# 成功：
# {"msg": "success", "code": 200, "data": {"username": "raidyue", "over": 51.0, "password": "123"}}
# 失败：
# {"msg": "", "code": 200, "data": {"username": "raidyue4"}}
#
def get_user_by_name(request, username):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse(response_result(code=ResponseCode.user_not_exist, msg='user not existed'))
        data = {'username': user.username, 'password': user.password, 'over': user.over}
        response_data = response_result(data=data)
        return HttpResponse(response_data)


# 添加用户 POST
# 参数:
# username 用户名
# password 用户密码
# email    邮件
#
# 成功：
# {"msg": "success", "code": 200, "data": {"username": "raidyue4"}}
#
# 失败：
# {"msg": "user existed", "code": 400, "data": {}}
#
def add_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
        except:
            return HttpResponse(response_result(code=ResponseCode.error_parameter, msg='username not in request'))
        password = request.POST['password']
        email = request.POST['email']
        if User.is_user_exist(username):
            return HttpResponse(response_result(code=ResponseCode.user_exist, msg='user existed'))
        user = User(username=username, password=password, email=email)
        user.save()
        return HttpResponse(response_result(data={'username': username}))


# 更新用户信息
# 参数：
# username 用户名(不可更改)
# password 用户密码
# email    邮件
#
#
def update_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    try:
        user = User.objects.get(username=username)
        user.password = password
        user.email = email
        # user.save()
        return HttpResponse(response_result(data={'username': username}))
    except User.DoesNotExist:
        return HttpResponse(response_result(code=ResponseCode.user_not_exist, msg='user not existed'))





