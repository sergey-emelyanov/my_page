from django.urls import path
from . import views

urlpatterns = [
    path('<week_day>', views.week_days),


]