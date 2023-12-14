from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Beer, Store, User
# Create your views here.

def beer_index(request):
  beers = Beer.objects.all()
  return render(request,'marketplace/beer_index.html', {'beers': beers })

def beer_show(request, id):
  beer = get_object_or_404(Beer, id=id)
  return render(request, 'marketplace/beer_show.html', {'beer': beer })

def profile(request):
    if request.user.is_authenticated:
        current_username = request.user.username
    else:
        current_username = None
    context = {'current_username': current_username}
    return render(request, 'marketplace/profile.html', context)
