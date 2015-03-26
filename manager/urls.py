from django.conf.urls import patterns, url
from views import order_manage_views

urlpatterns = patterns('',
                       url(r'^$', order_manage_views.index, name='manager_index'),
                       url(r'^login/$', order_manage_views.login, name='manager_login'),
                       url(r'^logout/$', order_manage_views.logout, name='manager_logout'),
                       url(r'^order/(?P<status>\d+)/$', order_manage_views.order, name='manager_order'),
                       url(r'^order/confirmation', order_manage_views.confirm_order, name='manager_order_confirmation')

                       )
