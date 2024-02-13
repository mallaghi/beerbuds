from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import StoreForm, BeerForm, CartItemForm, OrderItemForm
from .models import Beer, Store, User, CartItem, Cart, Profile, OrderItem, Order

# Create your views here.

def beer_index(request):
  beers = Beer.objects.all()
  return render(request,'marketplace/beer_index.html', {'beers': beers })

def beer_show(request, id):
  beer = get_object_or_404(Beer, id=id)
  return render(request, 'marketplace/beer_show.html', {'beer': beer })



def create_store(request):
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
   store = Store.objects.filter(user_id=request.user)
   return render(request, 'marketplace/store_dash.html', {'store': store})

def profile(request):
    if request.user.is_authenticated:
        current_username = request.user.username
    else:
        current_username = None
    context = {
        'current_username': current_username,
        }
    return render(request, 'marketplace/profile.html', context)

def create_beer(request):
    if request.method == "POST":
        beer = Beer(store_id=request.user.store)
        form = BeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            beer.save()
            return redirect('/store_dashboard')
    else:
        form = BeerForm()
    return render(request, 'marketplace/create_beer.html', {'form': form})


def add_to_cart(request, beer_id):
    user_profile = get_object_or_404(Profile, user_id=request.user)
    beer = get_object_or_404(Beer, id=beer_id)

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            user_carts = Cart.objects.filter(profile_id=user_profile)

            if user_carts[0]:
                user_cart = user_carts[0]
            else:
                user_cart = Cart.objects.create(profile_id=user_profile, total_price=0)
            cart_item = CartItem.objects.create(beer_id=beer, quantity=quantity)

            cart_item.save()
            user_cart.cart_items.add(cart_item)
            user_cart.calculate_total_price()
            return render(request, 'marketplace/user_cart.html', {'user_cart': user_cart})

    else:
        form = CartItemForm()
    return render(request, 'marketplace/add_to_cart.html', {'form': form, 'beer': beer})


def user_cart(request):
    user_profile = get_object_or_404(Profile, user_id=request.user)
    user_carts = Cart.objects.filter(profile_id=user_profile).first()

    return render(request, 'marketplace/user_cart.html', {'user_cart': user_carts})


def store_dash(request):
   store = Store.objects.filter(user_id=request.user)
   return render(request, 'marketplace/store_dash.html', {'store': store})

# this is what we can access from store_dash --> store and store info.
# so below line will not work

def delete_beer(request, id):
    beer = Beer.objects.get(pk=id)
    beer.delete()
    return redirect('/store_dashboard')

def add_to_order(request, beer_id):
    user_profile = get_object_or_404(Profile, user_id=request.user)
    beer = get_object_or_404(Beer, id=beer_id)

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            user_carts = Cart.objects.filter(profile_id=user_profile)

            if user_carts[0]:
                user_cart = user_carts[0]
            else:
                user_cart = Cart.objects.create(profile_id=user_profile, total_price=0)
            cart_item = CartItem.objects.create(beer_id=beer, quantity=quantity)

            cart_item.save()
            user_cart.cart_items.add(cart_item)
            user_cart.calculate_total_price()
            return render(request, 'marketplace/user_cart.html', {'user_cart': user_cart})

    else:
        form = CartItemForm()
    return render(request, 'marketplace/add_to_order.html', {'form': form, 'beer': beer})
