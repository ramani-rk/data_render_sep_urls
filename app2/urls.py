from django.contrib import admin
from django.urls import path
from app2.views import *
app_name = 'worldcup semi'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data2_render/',data2_render,name='data2_render'),
]