from django.conf.urls import patterns, url
from views import user_views, business_views

urlpatterns = patterns('',
                       url(r'^$', user_views.index, name='index'),
                       url(r'^register/$', user_views.register, name='register'),
                       url(r'^login/$', user_views.login, name='login'),
                       url(r'^logout/$', user_views.logout, name='logout'),
                       url(r'^user_order/(?P<page_id>\d+)/$', user_views.user, name='user_order'),
                       url(r'^user_info/', user_views.user_info, name='user_info'),

                       url(r'^order/$', business_views.order_lot, name='order_lot'),

                       # api
                       # url(r'^api/user/(?P<username>\w+)/$', api_views.index, name='api_user'),

                       # manager
                       # url(r'^manager/$', manager_views.index, name='manager_index'),
                       # url(r'^manager/login/$', manager_views.login, name='manager_login'),
                       # url(r'^manager/logout/$', manager_views.logout, name='manager_logout'),
                       # url(r'^manager/order/(?P<status>\d+)/$', manager_views.order, name='manager_order'),
                       # url(r'^manager/order/confirmation', manager_views.confirm_order,
                       # name='manager_order_confirmation')
                       )
