from django.urls import path
from . import views
app_name = 'user_actions'

urlpatterns = [
    path('<int:beer_id>/create_review/', views.create_review, name='create_review'),
    path('reviews_index/', views.reviews_index, name="reviews_index"),
    path('<int:id>/beer_reviews_index/', views.beer_reviews_index, name="beer_reviews_index"),
]
