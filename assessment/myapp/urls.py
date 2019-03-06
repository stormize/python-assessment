
from django.contrib import admin
from . import views
from django.urls import path
app_name="myapp"
urlpatterns = [
    path('', views.app,name="app"),
    path('profile', views.profile,name="profile"),
]
