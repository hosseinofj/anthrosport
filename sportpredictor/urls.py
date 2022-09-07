from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('information',views.get_information,name="informations"),
    path('height',views.get_height,name="height"),
    
]