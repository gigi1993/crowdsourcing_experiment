from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
#    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^success$', views.success, name='success'),
    url(r'^fail$', views.fail, name='fail'),
    url(r'^end$', views.end, name='end'),
    url(r'^finish', views.finish, name='finish'),
]