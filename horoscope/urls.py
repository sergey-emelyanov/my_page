from django.urls import path
from . import views
urlpatterns = [
    path('<sign_zodiack>',views.signs_of_zodiack),

]