from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^keyboard$', views.keyboard, name='keyboard'),
    url(r'^message$', views.message, name='message'),
    url(r'^friend$', views.friend, name='friend'),
]
