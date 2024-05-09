from django.urls import path
from . import views
from .views import ReviewDelete
app_name = 'user_actions'

urlpatterns = [
    path('<int:beer_id>/create_review/', views.create_review, name='create_review'),
    path('reviews_index/', views.reviews_index, name="reviews_index"),
    path('<int:beer_id>/beer_reviews_index/', views.beer_reviews_index, name="beer_reviews_index"),
    path('<int:beer_id>/add_favourite/', views.add_favourite, name="add_favourite"),
    path('favourites_index/', views.favourites_index, name="favourites_index"),
    path('<int:beer_id>/beer_favourites_index/', views.beer_favourites_index, name="beer_favourites_index"),
    path('<int:beer_id>/beer_reviews_index/delete/<int:pk>', ReviewDelete.as_view(), name="delete_review"),
    path('<int:beer_id>/delete_favourite/', views.delete_favourite, name="delete_favourite"),
    path('<int:beer_id>/delete_favourite/', views.delete_favourite, name="delete_favourite"),

]
