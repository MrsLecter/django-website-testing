from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('complete_purchase/', views.complete_purchase, name='complete_purchase'),
]