from django.shortcuts import render
from django.http import HttpResponse
from .models import Beer, Store, User
# Create your views here.

def beer_index(request):
  beers = Beer.objects.all()
  return render(request,'marketplace/beer_index.html', {'beers': beers })

