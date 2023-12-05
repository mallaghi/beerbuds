from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput
    (attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password = forms.CharField(widget=forms.PasswordInput
    (attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

# SignUpForm inherits from UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
                   'password1', 'password2']

    first_name = forms.CharField(widget=forms.TextInput
    (attrs={
        'placeholder': 'Your first name',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    last_name = forms.CharField(widget=forms.TextInput
    (attrs={
        'placeholder': 'Your last name',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    username = forms.CharField(widget=forms.TextInput
    (attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    email = forms.CharField(widget=forms.EmailInput
    (attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password1 = forms.CharField(widget=forms.PasswordInput
    (attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password2 = forms.CharField(widget=forms.PasswordInput
    (attrs={
        'placeholder': 'Confirm password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))
