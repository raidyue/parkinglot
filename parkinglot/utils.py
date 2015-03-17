def response_result(code=200, msg='', data={}):
    result = {'code': code, 'msg': msg, 'data': data}
    return result