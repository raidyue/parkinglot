from django.conf.urls import patterns, url
import views
urlpatterns = patterns('',
                       url(r'^user/(?P<username>\w+)/$', views.index, name='index'),

                       )
