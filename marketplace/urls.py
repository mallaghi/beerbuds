from django.urls import path
from . import views
app_name = 'marketplace'

urlpatterns= [
    path('beers/', views.beer_index)
]


