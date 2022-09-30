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
    path('fat',views.get_fat,name="fat"),
    path('back_flexibility',views.get_back_flexibility,name="back_flexibility"),
    path('shoulder_flexibility',views.get_shoulder_flexibility,name="shoulder_flexibility"),
    path('finger_ratio_2_4',views.get_finger_ratio_2_4,name="finger_ratio_2_4"),
    path('super_test',views.get_super_test,name="super_test"),
    path('result',views.take_result,name="result"),
    path('do',views.do,name="do"),
    
]