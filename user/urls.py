from django.urls import path
from .views import *


urlpatterns = [
    path('login', sign_in),
    path('dummy', get_dummy),
    path('logout', sign_out),
]
