from django.conf.urls import patterns, url
from views import user_apis

urlpatterns = patterns('',
                       # user
                       url(r'^user/info/(?P<username>\w+)', user_apis.get_user_by_name, name='get_user'),
                       url(r'^user/new', user_apis.add_user, name='new_user'),
                       url(r'^user/modification', user_apis.update_user, name='update_user'),
                       url(r'^user/order/(?P<username>\w+)/(?P<status>\d+)', user_apis.get_order_by_user,
                           name='get_order_by_user'),

                       # parkinglot
                       url(r'parkinglots', user_apis.get_all_parkinglot, name='get_all_parkinglots'),

                       # order
                       url(r'^order/new', user_apis.add_order, name='add_order'),
                       )
