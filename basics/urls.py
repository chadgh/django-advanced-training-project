from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='all'),
    url(r'^(?P<todo_id>[0-9]+)/done/$', views.mark_done, name='done'),
    url(r'^(?P<todo_id>[0-9]+)/undone/$', views.mark_not_done, name='undone'),
]
