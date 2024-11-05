

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('password/', views.password, name='password'),
    path('home/', views.home, name='home'),  # Home page or next page after registration
]
