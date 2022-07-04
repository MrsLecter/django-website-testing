from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.profiles, name='profiles'),
    path('users/login/', views.loginPage, name='login'),
    path('users/logout/', views.logoutPage, name='logout')
]