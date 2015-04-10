from django.contrib import admin
from models import *


class UserAdmin(admin.ModelAdmin):
    pass


class LotInline(admin.TabularInline):
    model = Lot
    extra = 12


class ParkinglotAdmin(admin.ModelAdmin):
    fields = ('name', 'city', 'address', 'charge')
    inlines = [LotInline]


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'parkinglot', 'lot', 'order_time')
    fields = ('user', 'parkinglot', 'lot', 'order_time', 'start_time', 'end_time')


admin.site.register(User)
admin.site.register(Parkinglot, ParkinglotAdmin)
admin.site.register(Lot)
admin.site.register(Order, OrderAdmin)
admin.site.register(Manager)
