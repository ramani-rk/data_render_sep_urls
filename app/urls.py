from django.contrib import admin
from django.urls import path
from app.views import *
app_name = 'worldcup'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data1_render/',data1_render,name='data1_render'),
]