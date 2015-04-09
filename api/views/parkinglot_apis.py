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
    data = {'parkinglot': parkinglot_id, 'free_lot': len(lots)}
    return response(data=data)