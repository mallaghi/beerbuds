from django.urls import path
from . import views
app_name = 'marketplace'

urlpatterns = [
    path('beers/', views.beer_index),
    path('beer/<int:id>/', views.beer_show, name='beer_show'),
    path('create_store/', views.create_store, name="create_store"),
    path('store_dashboard/', views.store_dash, name="store_dash"),
    path('profile/', views.profile, name='profile'),
    path('add_to_cart/<int:beer_id>/', views.add_to_cart, name='add_to_cart'),
    path('user_cart/', views.user_cart, name='user_cart'),
]
