from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^users',views.users,name='user registration'),
    url(r'^$', views.index, name='index'),
]
