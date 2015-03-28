# encoding=utf-8
import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    over = models.FloatField(default=0)
    email = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.username


class Parkinglot(models.Model):
    name = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    charge = models.FloatField(default=0)

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


class Lot(models.Model):
    parkinglot = models.ForeignKey(Parkinglot)
    num = models.CharField(max_length=10)
    status = models.IntegerField(default=0)

    def __unicode__(self):
        return self.parkinglot.name + '-' + self.num

    def use(self):
        self.status = 1


class Order(models.Model):
    user = models.ForeignKey(User)
    parkinglot = models.ForeignKey(Parkinglot)
    lot = models.ForeignKey(Lot)
    start_time = models.DateTimeField('start parking time', null=True)
    end_time = models.DateTimeField('end parking time', null=True)
    order_time = models.DateTimeField('order time', null=True)
    # 0=on_order 1=parking 2=finished(leave) 3=failed
    status = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username + '-' + self.parkinglot.name

    # 判定订单是否有效（从预定开始到当前时间小于20分钟则有效，反之无效）,返回True有效,False无效
    def isValid(self):
        return self.order_time >= timezone.now() - datetime.timedelta(minutes=20)

    @staticmethod
    def remove_invalid_orders():
        orders = [order for order in Order.objects.all() if not order.isValid()]
        for order in orders:
            lot = order.lot
            lot.status = 0
            lot.save()


class Manager(models.Model):
    parkinglot = models.ForeignKey(Parkinglot)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
