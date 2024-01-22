# from django.shortcuts import render , redirect , get_object_or_404
# from marketplace.models import Profile
# from .models import Review, Beer
# from .forms import ReviewForm

# # Create your views here.
# def create_review(request):
#     if request.method == 'POST':
#         profile = Profile(user_id=request.user)
#         beer = get_object_or_404(Beer, id=id)
#         beer_id = beer.id
#         review = Review(profile_id=profile, beer_id=beer_id)
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             review.save()
#             # messages.success("Successfully added!")
#             # Redirect to the store dashboard template or another page upon successful creation
#             return redirect('/review_index')
#     else:
#         form = ReviewForm()
#     return render(request, 'user_actions/create_review.html', {'form': form})

# views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from marketplace.models import Profile
# from .models import Review, Beer
# from .forms import ReviewForm

# def create_review(request, beer_id,):
#     profile = Profile(user_id=request.user)
#     beer = get_object_or_404(Beer, id=beer_id)

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.profile = profile
#             review.beer = beer
#             review.save()
#             return redirect('/beer_index')
#     else:
#         form = ReviewForm()

#     return render(request, 'user_actions/create_review.html', {'form': form, 'beer': beer})

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from marketplace.models import Profile
from .models import Review, Beer
from .forms import ReviewForm

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

def beer_reviews_index(request,id):
    reviews = Review.objects.filter(beer_id=id)
    return render(request, 'user_actions/beer_reviews_index.html', {'beer_reviews': reviews})
