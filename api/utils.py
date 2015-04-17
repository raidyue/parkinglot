from django.http import HttpResponse
import json


def response(code=0, msg='success', data=''):
    result = {'code': code, 'msg': msg, 'data': data}
    response_data = json.dumps(result)
    return HttpResponse(response_data)


class ResponseCode(object):
    user_not_exist = 401
    user_exist = 400
    error_parameter = 402
    pl_is_full = 403
    pl_not_exist = 404
    order_transaction_exception = 405
    unclear_except = 406
    insufficient_funds = 407
    have_uncomfirmed_order = 408


