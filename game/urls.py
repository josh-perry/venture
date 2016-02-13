from django.conf.urls import url
from django.contrib import admin

from game import views

urlpatterns = [
    url(r'^$', views.RootView.as_view())
]
