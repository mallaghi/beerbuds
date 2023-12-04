from django.shortcuts import render
from django.http import HttpResponse
from .models import Store, Beer, Profile


def beer_index(request):
  beers = Beer.objects.all()
  return render(request,'marketplace/beer_index.html', {'beers': beers })
