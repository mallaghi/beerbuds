from django.shortcuts import render, redirect
from .forms import SignupForm
from marketplace.models import Profile
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user_id=user,address='')
            return redirect('/login')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
