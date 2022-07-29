from django.urls import path
from . import views
urlpatterns = [
    path('<int:sign_zodiack>',views.signs_of_zodiack_by_int),
    path('<str:sign_zodiack>',views.signs_of_zodiack_by_str),

]