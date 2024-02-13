from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from marketplace.models import Profile
from .models import Review, Beer, Favourite
from .forms import ReviewForm, FavouriteForm
from django.db import IntegrityError

def create_review(request, beer_id):
    # Get the user's profile
    profile = get_object_or_404(Profile, user_id=request.user)

    # Get the beer object
    beer = get_object_or_404(Beer, id=beer_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.profile_id = profile
            review.beer_id = beer
            review.save()

            redirect_url = reverse('marketplace:beer_show', kwargs={'id': beer_id})
            return redirect(redirect_url)
    else:
        form = ReviewForm()

    return render(request, 'user_actions/create_review.html', {'form': form, 'beer': beer})

def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'user_actions/reviews_index.html', {'all_reviews': reviews})

def beer_reviews_index(request,beer_id):
    reviews = Review.objects.filter(beer_id=beer_id)
    return render(request, 'user_actions/beer_reviews_index.html', {'beer_reviews': reviews})

def add_favourite(request, beer_id):
    # Get the user's profile
    profile = get_object_or_404(Profile, user_id=request.user)

    # Get the beer object
    beer = get_object_or_404(Beer, id=beer_id)

    if request.method == 'POST':
        form = FavouriteForm(request.POST)
        if form.is_valid():
            try:
                favourite = form.save(commit=False)
                favourite.profile_id = profile
                favourite.beer_id = beer
                favourite.save()
                redirect_url = reverse('marketplace:beer_show', kwargs={'id': beer_id})
                return redirect(redirect_url)
            except IntegrityError:
                form.add_error(None, "You have already favourited this beer.")
    else:
        form = FavouriteForm()

    return render(request, 'user_actions/add_favourite.html', {'form': form, 'beer': beer})



def favourites_index(request):
    favourites = Favourite.objects.all()
    return render(request, 'user_actions/favourites_index.html', {'all_favourites': favourites})

def beer_favourites_index(request,beer_id):
    favourites = Favourite.objects.filter(beer_id=beer_id)
    return render(request, 'user_actions/beer_favourites_index.html', {'beer_favourites': favourites})
