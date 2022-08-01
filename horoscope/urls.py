from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('type', views.type),
    path('type/<str:element>',views.elements, name='element_types'),
    path('<int:sign_zodiack>',views.signs_of_zodiack_by_int),
    path('<str:sign_zodiack>',views.signs_of_zodiack_by_str, name='horoscope_names'),

]