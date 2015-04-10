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


admin.site.register(User)
admin.site.register(Parkinglot, ParkinglotAdmin)
admin.site.register(Lot)
admin.site.register(Order)
admin.site.register(Manager)
