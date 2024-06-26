from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from marketplace.models import Profile
from .models import Review, Beer, Favourite
from .forms import ReviewForm, FavouriteForm
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib import messages

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
        favourites_form = FavouriteForm(request.POST)
        if favourites_form.is_valid():
            try:
                favourite = favourites_form.save(commit=False)
                favourite.profile_id = profile
                favourite.beer_id = beer
                favourite.save()
                return redirect(reverse('marketplace:beer_show', kwargs={'id': beer_id}))
            except IntegrityError:
                favourites_form.add_error(None, "You have already favourited this beer.")
    else:
        favourites_form = FavouriteForm()

    # return render(request, 'marketplace/beer_show.html', {'favourites_form': favourites_form, 'beer': beer})
    return render(request, 'marketplace/beer_show.html', {'favourites_form': favourites_form, 'beer': beer})


def favourites_index(request):
    favourites = Favourite.objects.all()
    return render(request, 'user_actions/favourites_index.html', {'all_favourites': favourites})

def beer_favourites_index(request,beer_id):
    favourites = Favourite.objects.filter(beer_id=beer_id)
    return render(request, 'user_actions/beer_favourites_index.html', {'beer_favourites': favourites})

class ReviewDelete(DeleteView):
    model = Review
    # get the url to redirect to the beer_reviews_index page
    def get_success_url(self):
        beer_id = self.kwargs['beer_id']
        return reverse_lazy('user_actions:beer_reviews_index', kwargs={'beer_id': beer_id})

    def form_valid(self, form):
        messages.success(self.request, "The review was deleted successfully.")
        return super(ReviewDelete,self).form_valid(form)

def delete_favourite(request, beer_id):
    # Get the current user's profile
    profile = get_object_or_404(Profile, user_id=request.user)
    # Get the beer object
    beer = get_object_or_404(Beer, id=beer_id)
    # Get the favourite object for the specified beer and profile
    favourite = get_object_or_404(Favourite, beer_id=beer, profile_id=profile)
    # Delete the favourite object
    favourite.delete()
    # Redirect to a relevant URL, for example, the beer show page
    return redirect(reverse('marketplace:beer_show', kwargs={'id': beer_id}))
