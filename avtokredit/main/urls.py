from django.urls import path
from .views import *


urlpatterns = [
    path('credit/', credit),
    path('login', log_in),
    path('sign_up', sign_up)
    ]