from django.conf.urls import patterns, url
from views import user_apis

urlpatterns = patterns('',
                       url(r'^user/info/(?P<username>\w+)/$', user_apis.get_user_by_name, name='get_user'),
                       url(r'^user/new/$', user_apis.add_user, name='new_user'),
                       )
