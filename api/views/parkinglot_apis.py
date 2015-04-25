# encoding=utf-8
from ..utils import *
from parkinglot.models import *


def parkinglot_free_lot(request, parkinglot_id):
    Order.remove_invalid_orders()
    try:
        parkinglot = Parkinglot.objects.get(id=parkinglot_id)
    except Parkinglot.DoesNotExist:
        return response(code=ResponseCode.pl_not_exist, msg='parkinglot not exist')
    lots = [lot for lot in Lot.objects.filter(parkinglot=parkinglot) if lot.status == 0]
    data = {'p_id': parkinglot.id, 'free': len(lots)}
    return response(data=data)


# 获取停车场列表 GET
#
# 成功
# {"msg": "success", "code": 200, "data": [{"city": "hn", "charge": 2.0, "name": "parkinglot1", "address": "cd"}, {"city": "beijing", "charge": 1.0, "name": "parkinglot2",
# "address": "beijing"}]}
# {"msg": "success", "code": 200, "data": []}
#
def get_all_parkinglot(request):
    parkinglot_dict = [pl.to_dict() for pl in Parkinglot.objects.all()]
    return response(data=parkinglot_dict)