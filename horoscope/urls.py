from django.urls import path, register_converter
from . import views,converters

register_converter(converters.MyCustomFloatConverter, 'float')


urlpatterns = [
    path('keanu', views.keanu),
    path('guinness', views.get_guinness_world_records),
    path('type', views.type),
    path('type/<str:element>',views.elements, name='element_types'),
    path('<int:sign_zodiack>',views.signs_of_zodiack_by_int),
    path('<float:value>', views.float_value),
    path('<str:sign_zodiack>',views.signs_of_zodiack_by_str, name='horoscope_names'),

]