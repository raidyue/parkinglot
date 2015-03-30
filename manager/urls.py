from django.conf.urls import patterns, url
from views import manager_views, manager_parkinglot

urlpatterns = patterns('',
                       url(r'^$', manager_views.index, name='manager_index'),
                       url(r'^login/$', manager_views.login, name='manager_login'),
                       url(r'^logout/$', manager_views.logout, name='manager_logout'),
                       url(r'^order/(?P<status>\d+)/(?P<page_id>\d+)/$', manager_views.order, name='manager_order'),
                       url(r'^order/confirmation', manager_views.confirm_order, name='manager_order_confirmation'),
                       url(r'^order/leave', manager_views.parking_leave, name='manager_order_parking_leave'),
                       url(r'^parkinglot', manager_parkinglot.parkinglot_info, name='manager_parkinglot'),

                       )
