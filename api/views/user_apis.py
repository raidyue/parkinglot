# encoding=utf-8
from ..utils import *
from parkinglot.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.db import transaction
from django.db.transaction import TransactionManagementError


# Create your views here.

# 根据用户名获取用户信息 GET
# 参数:
# username 用户名
# 成功：
# {"msg": "success", "code": 200, "data": {"username": "raidyue", "over": 51.0, "password": "123"}}
# 失败：
# 用户已存在 {"msg": "", "code": 200, "data": {"username": "raidyue4"}}
def get_user_by_name(request, username):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return response(code=ResponseCode.user_not_exist, msg='user not existed')
        return response(data=user.to_dict())


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
# 用户已存在 {"msg": "user existed", "code": 400, "data": {}}
# 参数不完全 {"msg": "need parameter username,password,email in request", "code": 402, "data": {}}
#
def add_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except MultiValueDictKeyError:
            return response(code=ResponseCode.error_parameter, msg='need parameter username,password,email in request')
        if User.is_user_exist(username):
            return response(code=ResponseCode.user_exist, msg='user existed')
        user = User(username=username, password=password, email=email)
        user.save()
        return response(data={'username': username})


# 更新用户信息 POST
# 参数：
# username 用户名(不可更改)
# password 用户密码
# email    邮件
#
# 成功：
# {"msg": "success", "code": 200, "data": {"username": "raidyue"}}
#
# 失败：
# 参数错误 {"msg": "need parameter username,password,email in request", "code": 402, "data": {}}
# 用户不存在 {"msg": "user not existed", "code": 401, "data": {}}
#
def update_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except MultiValueDictKeyError:
            return response(code=ResponseCode.error_parameter, msg='need parameter username,password,email in request')
        try:
            user = User.objects.get(username=username)
            user.password = password
            user.email = email
            user.save()
            return response(data={'username': username})
        except User.DoesNotExist:
            return response(code=ResponseCode.user_not_exist, msg='user not existed')


# 根据用户username获取用户订单
# 参数：
# username 用户名
# status # 0=ordering 1=parking 2=finished 3=aborted 4=all
#
# 成功
# {"msg": "success", "code": 200, "data": [{"status": 0, "order_time": "2015-03-28 10:54:21", "start_time": "0000-00-00 00:00:00", "parkinglot": "parkinglot1",
# "end_time": "0000-00-00 00:00:00", "lot": "1", "user": "raidyue"}, ]
#
# 没有订单 {"msg": "success", "code": 200, "data": []}
#
# 失败
# 用户不存在 {"msg": "user not exist", "code": 401, "data": ""}
# status错误 {"msg": "status not in [0,1,2,3,4]", "code": 402, "data": ""}
#
def get_order_by_user(request, username, status):
    if request.method == 'GET':
        try:
            status = int(status)
            user = User.objects.get(username=username)
        except ValueError:
            return response(code=ResponseCode.error_parameter, msg='status not in [0,1,2,3,4]')
        except User.DoesNotExist:
            return response(code=ResponseCode.user_not_exist, msg='user not exist')
        if status == 4:
            orders_dict = [order.to_dict() for order in Order.objects.filter(user=user)]
        elif status == 0:
            orders_dict = [order.to_dict() for order in Order.objects.filter(user=user) if
                           order.is_valid() and order.status == 0]
        elif status == 1:
            orders_dict = [order.to_dict() for order in Order.objects.filter(user=user) if order.status == 1]
        elif status == 2:
            orders_dict = [order.to_dict() for order in Order.objects.filter(user=user) if order.status == 2]
        elif status == 3:
            orders_dict = [order.to_dict() for order in Order.objects.filter(user=user) if
                           not order.is_valid() and order.status == 0]
        else:
            return response(code=ResponseCode.error_parameter, msg='status not in [0,1,2,3,4]')
        return response(data=orders_dict)


# 获取停车场列表 GET
#
# 成功
# {"msg": "success", "code": 200, "data": [{"city": "hn", "charge": 2.0, "name": "parkinglot1", "address": "cd"}, {"city": "beijing", "charge": 1.0, "name": "parkinglot2",
# "address": "beijing"}]}
# {"msg": "success", "code": 200, "data": []}
#
def get_parkinglots(request):
    parkinglot_dict = [pl.to_dict() for pl in Parkinglot.objects.all()]
    return response(data=parkinglot_dict)


# 添加订单 POST
# 参数
# username        用户名
# parkinglot_id   停车场id
#
# 成功
# {"msg": "success", "code": 200, "data": {"status": 0, "order_time": "2015-04-01 10:00:50", "start_time": "0000-00-00 00:00:00", "parkinglot": "parkinglot1", "end_time": "0000-00-00 00:00:00", "lot": "1", "user": "raidyue"}}
#
#
@transaction.commit_manually
def add_order(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            parkinglot_id = request.POST['parkinglot_id']
            user = User.objects.get(username=username)
            parkinglot = Parkinglot.objects.get(id=parkinglot_id)
            lot = parkinglot.get_unused_lot()
            if lot is None:
                return response(code=ResponseCode.pl_is_full, msg='parkinglot is full')
            order = Order(user=user, parkinglot=parkinglot, lot=lot, order_time=timezone.now())
        except MultiValueDictKeyError:
            return response(code=ResponseCode.error_parameter, msg='need username and parkinglot_id')
        except User.DoesNotExist:
            return response(code=ResponseCode.user_not_exist, msg='user not exist')
        except Parkinglot.DoesNotExist:
            return response(code=ResponseCode.pl_not_exist, msg='parkinlot not exist')
        except:
            return response(code=ResponseCode.unclear_except, msg='i do not know why')
        try:
            lot.status = 1
            lot.save()
            order.save()
        except TransactionManagementError:
            transaction.rollback()
            return response(code=ResponseCode.order_transaction_exception, msg='transaction manager error')
        else:
            transaction.commit()
        return response(data=order.to_dict())







