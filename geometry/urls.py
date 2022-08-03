from django.urls import path
from . import views

urlpatterns = [
    path('people', views.people),
    path('rectangle/<int:length>/<int:width>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:length>',views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area,name='circle'),
    path('get_rectangle_area',views.rectangle_area),
    path('get_square_area',views.square_area),
    path('get_circle_area',views.circle_area)
    ]