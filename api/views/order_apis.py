# encoding=utf-8
from ..utils import *
from parkinglot.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.db import transaction
from django.db.transaction import TransactionManagementError

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
        Order.remove_invalid_orders()
        try:
            username = request.POST['username']
            parkinglot_id = request.POST['parkinglot_id']
            user = User.objects.get(username=username)
            parkinglot = Parkinglot.objects.get(id=parkinglot_id)
            lot = parkinglot.get_unused_lot()
            if user.have_unfinished_order(parkinglot):
                transaction.commit()
                return response(code=ResponseCode.have_uncomfirmed_order, msg='have unfinished order')
            if parkinglot.charge > user.over:
                transaction.commit()
                return response(code=ResponseCode.insufficient_funds, msg='insufficient funds')
            if lot is None:
                transaction.commit()
                return response(code=ResponseCode.pl_is_full, msg='parkinglot is full')
            order = Order(user=user, parkinglot=parkinglot, lot=lot, order_time=timezone.now())
        except MultiValueDictKeyError:
            transaction.commit()
            return response(code=ResponseCode.error_parameter, msg='need username and parkinglot_id')
        except User.DoesNotExist:
            transaction.commit()
            return response(code=ResponseCode.user_not_exist, msg='user not exist')
        except Parkinglot.DoesNotExist:
            transaction.commit()
            return response(code=ResponseCode.pl_not_exist, msg='parkinlot not exist')
        except Exception,e:
            transaction.commit()
            print e
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