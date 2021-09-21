from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'), 
    path('someview', views.some_view, name='some_view'),
]