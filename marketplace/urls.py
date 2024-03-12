import re
from django.urls import path, re_path
from . import views
app_name = 'marketplace'

urlpatterns = [
    path('beers/', views.beer_index, name='beer_index'),
    path('beer/<int:id>/', views.beer_show, name='beer_show'),
    path('create_store/', views.create_store, name="create_store"),
    path('store_dashboard/', views.store_dash, name="store_dash"),
    path('profile/', views.profile, name='profile'),
    path('add_to_cart/<int:beer_id>/', views.add_to_cart, name='add_to_cart'),
    path('user_cart/', views.user_cart, name='user_cart'),
    path('store_dashboard/create_beer/', views.create_beer, name="create_beer"),
    path('profile/', views.profile, name='profile'),
    path('store_dashboard/delete_beer/<int:id>', views.delete_beer, name="delete_beer"),
    path('add_to_order/', views.add_to_order, name='add_to_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order_history/', views.order_history, name='order_history'),
]
