# 停车场预定管理系统（服务器）
## 目录说明
- doc （文档目录）
 - 需求分析
 - 数据库字段
 - 数据库设计说明
- requirements.txt （当前用到的python package以及版本）


Parkinglot API

# 获取用户信息
- GET 请求：[http://xxx.xxx.xxx.xxx:port/api/user/info/'username']
- 参数：
    - username:用户名
- 注意：
    - username是url的一部分
    - username必须传入
- 返回json，示例如下：
```
{
  "msg": "success",   //当前状态信息，请求成功
  "code": 200,        //状态码，请求成功    
  "data": {           //返回内容
    "username": "raidyue",   //查询用户名
    "over": 51,              // 账户余额
    "password": "123",       // 密码（还未做加密处理）
    "email": "a@a"           // 用户邮件
  }
}
```
- 可能出现的错误：
```
{
  "msg": "user not existed", //查询的用户不存在
  "code": 401,
  "data": ""
}
```

# 添加用户
- POST 请求: [http://xxx.xxx.xxx.xxx:port/api/user/new]
- 参数：
    - username:用户名
    - password:密码
    - email:邮箱
- 注意：
    - 以上三个参数必须同时传入
    - username唯一，不允许相同
- 返回json，结果如下：
```
{
  "msg": "success",
  "code": 200,
  "data": {
    "username": "raidyue4"
  }
}
```
- 可能出现的错误：
```
//用户已存在
{
  "msg": "user existed",
  "code": 400,
  "data": {}
}
```
```
// 参数错误
{
  "msg": "need parameter username,password,email in request",
  "code": 402,
  "data": {}
}
```

# 更新用户信息
- POST 请求: [http://xxx.xxx.xxx.xxx:port/api/user/modification]
- 参数：
    - username:用户名
    - password:密码
    - email:邮箱
- 注意：
    - 以上三个参数必须同时传入
    - username作为查询条件，不可更改
- 返回json，结果如下：
```
{
  "msg": "success",
  "code": 200,
  "data": {
    "username": "raidyue"
  }
}
```
- 可能出现的错误：
```
//该用户不存在
{
  "msg": "user not existed",
  "code": 401,
  "data": {}
}
```
```
// 参数错误
{
  "msg": "need parameter username,password,email in request",
  "code": 402,
  "data": {}
}
```

# 根据用户用户名获取用户订单
- GET 请求: [http://xxx.xxx.xxx.xxx:port/api/user/order/'username'/'status']
- 参数：
    - username:用户名
    - status:订单状态 0=预定订单 1=停车中 2=订单结束（停车离开） 3=失效（超时） 4=全部订单
- 注意：
    - username&status必须存在
    - username作为查询条件
- 返回json，结果如下：
```
{
  "msg": "success",
  "code": 200,
  "data": [
    {
      "status": 2,
      "order_time": "2015-03-28 10:53:51",
      "start_time": "2015-03-28 10:53:58",
      "parkinglot": "parkinglot1",
      "end_time": "2015-03-28 10:54:01",
      "lot": "1",
      "user": "raidyue"
    },
    ...... 
  ]
}
```
```
//没有订单
{
  "msg": "success",
  "code": 200,
  "data": []
}
```
- 可能出现的错误：
```
//该用户不存在
{
  "msg": "user not exist",
  "code": 401,
  "data": ""
}
```
```
// 参数错误
{
  "msg": "status not in [0,1,2,3,4]",
  "code": 402,
  "data": ""
}
```


# 添加订单
- POST 请求: [http://xxx.xxx.xxx.xxx:port/api/order/new]
- 参数：
    - username:用户名
    - parkinglot_id:停车场id
- 注意：
    - username&parkinglot_id必须同时请求
- 返回json，结果如下：
```
{
  "msg": "success",
  "code": 200,
  "data": {
    "status": 0,
    "order_time": "2015-04-02 06:50:04",
    "start_time": "0000-00-00 00:00:00",
    "parkinglot": "parkinglot1",
    "end_time": "0000-00-00 00:00:00",
    "lot": "1",
    "user": "raidyue"
  }
}
```
- 可能出现的错误：
```
//参数错误
{
  "msg": "need username and parkinglot_id",
  "code": 402,
  "data": ""
}
```
```
//存在未确认的订单（短时间内不能重复提交订单）
{
  "msg": "have uncomfirmed order",
  "code": 408,
  "data": ""
}
```
```
//余额不足
{
  "msg": "insufficient funds",
  "code": 407,
  "data": ""
}
```
```
//停车场已满
{
  "msg": "parkinglot is full",
  "code": 403,
  "data": ""
}
```
```
//该用户不存在
{
  "msg": "user not exist",
  "code": 401,
  "data": ""
}
```
```
//错误的停车场（该停车场不存在）
{
  "msg": "parkinlot not exist",
  "code": 404,
  "data": ""
}
```