from django.urls import path
from . import views

urlpatterns = [
    path('subscribe', views.new_sub, name='subscribe'),
]