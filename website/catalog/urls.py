from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact_page, name='contact_page'),
    path('category/', views.category, name='category'),
    path('category/<str:category>', views.current_category, name='current_category'),
    path('item/<str:id>', views.current_item, name='current_item'),
    path('item/<str:id>/add', views.add_current_item, name='add_current_item'),
    path('checkout/', views.checkout, name='checkout')
]