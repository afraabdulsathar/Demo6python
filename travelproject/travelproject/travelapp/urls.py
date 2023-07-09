from . import views
from django.urls import path

urlpatterns = [

    path('',views.cemo,name='cemo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.addition,name='subtraction'),
    # path('mul/',views.addition,name='multiplication'),
    # path('div/',views.addition,name='division'),
    ]