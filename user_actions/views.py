from django.shortcuts import render , redirect
from marketplace.models import Profile
from .models import Review, Beer
from .forms import ReviewForm

# Create your views here.
def create_review(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        beer_id = request.POST.get('beer_id')
        review = Review(profile_id=profile, beer_id=beer_id)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.save()
            # messages.success("Successfully added!")
            # Redirect to the store dashboard template or another page upon successful creation
            return redirect('/review_index')
    else:
        form = ReviewForm()
    return render(request, 'user_actions/create_review.html', {'form': form})
