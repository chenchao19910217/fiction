from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index, name='index'),

    path('', views.login, name='login'),

    path('register/', views.register, name='register'),

    path('logout/', views.logout, name='logout'),

    path('personal/', views.personal, name='personal'),

    path('head_images/', views.head_images, name='head_images'),

]