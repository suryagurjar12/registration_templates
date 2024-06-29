from django.urls import path
# from surya_app import views
from .views import *


urlpatterns = [
    path('',register),
    path('registration/',registrationdata ,name='Registration'),
]