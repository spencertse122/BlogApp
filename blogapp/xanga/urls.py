from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('some_view', views.some_view, name='some_view'),
]

