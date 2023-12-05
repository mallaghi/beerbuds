from . import views
from django.urls import path, include
app_name = 'core'

urlpatterns = [
    path('signup/', views.signup, name="signup")
]
