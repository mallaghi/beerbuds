from django.urls import path
from . import views
app_name = 'user_actions'

urlpatterns = [
    path('<int:beer_id>/create_review/', views.create_review, name='create_review'),
    # path('review_index/', views.reviews_index, name="reviews_index"),
]
