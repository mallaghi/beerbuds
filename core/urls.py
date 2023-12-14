from . import views
from django.urls import path, include
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
        authentication_form=LoginForm), name='login'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]
