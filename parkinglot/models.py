# encoding=utf-8
from django.db import models
from django.utils import timezone
import datetime
from utils import *


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name=u'用户名')
    password = models.CharField(max_length=20, verbose_name=u'密码')
    over = models.FloatField(default=0, verbose_name=u'余额')
    email = models.CharField(max_length=50, default='', verbose_name=u'邮箱')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    def __unicode__(self):
        return self.username

    # 返回True则表示存在有效的订单，不能重复添加
    # 当用户在该停车场存在订单，订单还在有效时间内，则无法再次提交订单
    def have_unfinished_order(self, parkinglot):
        orders = Order.objects.filter(user=self, parkinglot=parkinglot).order_by('-order_time')
        if len(orders) <= 0:
            return False
        for order in orders:
            if (order.status == 0 and order.is_valid()) or order.status == 1:
                return True
        return False

    def to_dict(self):
        return {'user_id': self.id, 'username': str(self.username), 'password': str(self.password), 'over': self.over,
                'email': str(self.email)}

    # True表示用户存在，False表示用户不存在
    @staticmethod
    def is_user_exist(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return False
        return True


class Parkinglot(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'停车场名称')
    city = models.CharField(max_length=20, verbose_name=u'所在城市')
    address = models.CharField(max_length=80, verbose_name=u'地址')
    charge = models.FloatField(default=0, verbose_name=u'费用')

    class Meta:
        verbose_name = u'停车场'
        verbose_name_plural = u'停车场'

    def __unicode__(self):
        return self.name

    def get_unused_lot(self):
        all_lots = self.lot_set.filter(status=0)
        if len(all_lots) > 0:
            return all_lots[0]
        return None

    def is_full(self):
        all_lots = self.lot_set.filter(status=0)
        return len(all_lots) <= 0

    def to_dict(self):
        return {'name': str(self.name), 'city': str(self.city), 'address': str(self.address), 'charge': self.charge,
                'p_id': self.id
                }

    # 判断name是否存在，存在返回False,不存在返回True
    @staticmethod
    def is_parkinglot_not_exist(name):
        try:
            Parkinglot.objects.get(name=name)
        except Parkinglot.DoesNotExist:
            return True
        return False


class Lot(models.Model):
    parkinglot = models.ForeignKey(Parkinglot, verbose_name=u'所属停车场')
    num = models.CharField(max_length=10, verbose_name=u'编号')
    # 0=空位 1=使用中
    status = models.IntegerField(default=0, verbose_name=u'当前状态0为空闲，1为使用')

    class Meta:
        verbose_name = u'车位'
        verbose_name_plural = u'车位'

    def __unicode__(self):
        return self.parkinglot.name + '-' + self.num

    # 判断num是否存在，存在返回True，不存在返回False
    @staticmethod
    def is_lot_exist(num):
        try:
            Lot.objects.get(num=num)
        except Lot.DoesNotExist:
            return False
        return True


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    parkinglot = models.ForeignKey(Parkinglot, verbose_name=u'停车场')
    lot = models.ForeignKey(Lot, verbose_name=u'车位')
    start_time = models.DateTimeField(null=True, verbose_name=u'开始停车时间')
    end_time = models.DateTimeField(null=True, verbose_name=u'结束停车时间')
    order_time = models.DateTimeField(null=True, verbose_name=u'下单时间')
    # 0=加上时间对订单有效性进行判断 1=parking 2=finished(leave) 3=用户确认离开，用户确认离开以后管理员才能确认离开
    status = models.IntegerField(default=0, verbose_name=u'订单状态')

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = u'订单'

    def __unicode__(self):
        return str(self.id)

    # 判定订单是否有效（从预定开始到当前时间小于20分钟则有效，反之无效）,返回True有效,False无效
    def is_valid(self):
        return timezone.now() - self.order_time <= datetime.timedelta(minutes=20)

    def to_dict(self):
        return {'user': str(self.user.username), 'parkinglot': str(self.parkinglot.name), 'lot': str(self.lot.num),
                'start_time': date_format(self.start_time), 'end_time': date_format(self.end_time),
                'order_time': date_format(self.order_time), 'status': self.status, 'order_id': self.id,
                'user_id': self.user.id, 'p_id': self.parkinglot.id}

    def leave(self):
        try:
            if self.status == 1:
                self.status = 3
                self.save()
        except:
            return False
        return True

    @staticmethod
    def remove_invalid_orders():
        for order in Order.objects.filter(status=0):
            if not (order.is_valid()):
                lot = order.lot
                lot.status = 0
                lot.save()


class Manager(models.Model):
    parkinglot = models.ForeignKey(Parkinglot, verbose_name=u'所属停车场')
    name = models.CharField(max_length=20, unique=True, verbose_name=u'管理员名')
    password = models.CharField(max_length=20, verbose_name=u'管理员密码')

    class Meta:
        verbose_name = u'管理员'
        verbose_name_plural = u'管理员'

    def __unicode__(self):
        return self.parkinglot.name + '-' + self.name
