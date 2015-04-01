import json

def response_result(code=200, msg='success', data={}):
    result = {'code': code, 'msg': msg, 'data': data}
    response_data = json.dumps(result)
    return response_data


class ResponseCode(object):
    user_not_exist = 401
    user_exist = 400
    error_parameter = 402
