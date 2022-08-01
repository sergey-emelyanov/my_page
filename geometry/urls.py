from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:length>/<int:width>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:length>',views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area,name='circle'),
    path('get_rectangle_area/<int:length>/<int:width>',views.rectangle_area),
    path('get_square_area/<int:length>',views.square_area),
    path('get_circle_area/<int:radius>',views.circle_area)
    ]