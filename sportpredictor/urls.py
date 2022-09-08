from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('information',views.get_information,name="informations"),
    path('height',views.get_height,name="height"),
    path('weight',views.get_weight,name="weight"),
    path('armspan',views.get_armspan,name="armspan"),
    path('foot_length',views.get_foot_length,name="foot_length"),
    path('one_hand_length',views.get_one_hand_length,name="one_hand_length"),
    path('shoulder_size',views.get_shoulder_size,name="shoulder_size"),
    path('result',views.take_result,name="result"),
    
]