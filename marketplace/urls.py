from django.urls import path
from . import views
app_name = 'marketplace'

urlpatterns = [
    path('beers/', views.beer_index),
    path('beer/<int:id>/', views.beer_show, name='beer_show'),
    path('create_store/', views.create_store, name="create_store")
]

