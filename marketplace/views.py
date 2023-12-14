from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import StoreForm
from .models import Beer, Store, User

# Create your views here.

def beer_index(request):
  beers = Beer.objects.all()
  return render(request,'marketplace/beer_index.html', {'beers': beers })

def beer_show(request, id):
  beer = get_object_or_404(Beer, id=id)
  return render(request, 'marketplace/beer_show.html', {'beer': beer })

def create_store(request):
    # if you have a store, then the form will not appear and you will get an error message or redirected to home

    if request.method == 'POST':
        store = Store(user_id=request.user)
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store.save()
            # messages.success("Successfully added!")
            # Redirect to the store dashboard template or another page upon successful creation
            return redirect('/store_dashboard')
    else:
        form = StoreForm()
    return render(request, 'marketplace/create_store.html', {'form': form})

def store_dash(request):
   # multiple store dashboard
   stores = Store.objects.all()
   return render(request, 'marketplace/store_dash.html', {'stores': stores})
