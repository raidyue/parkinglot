# 停车场预定管理系统（服务器）
## 目录说明

### doc （文档目录）
- 需求分析
- 数据库字段
- 数据库设计说明
- requirements.txt （当前用到的python package以及版本）

## 项目说明
项目主要部分(对应各个文件夹)：

- api：接口
- manager:管理员部分
- parkinglot：项目的主体，也就是用户部分
 - migrations:数据库相关文件
 - static：js和css文件
 - templates：html文件
 - templatetags：自定义的filter
 - views：主要逻辑
 - urls.py：路由
 - models.py：ORM类定义（所有的model定义在parkinglot中）
- parkinglot_ms:项目文件夹，包含项目配置文件
 - settings.py
 
 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  //表示使用mysql
        'NAME': 'parkinglot_db',//数据库名
        'USER': 'root',//用户名
        'PASSWORD': '',//密码
    }
}
 ```
 
 

Parkinglot API 见wiki




