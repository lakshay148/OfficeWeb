from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users', views.users, name='user registration'),
    url(r'^tasks', views.tasks, name='user tasks'),
    url(r'^roles', views.roles, name='user roles'),
    url(r'^modules', views.modules, name='user modules'),
    url(r'^domains', views.domains, name='user domains'),
    url(r'^priviliges', views.priviliges, name='user priviliges'),
    url(r'^$', views.index, name='index'),
]
