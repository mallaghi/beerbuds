from django import forms
from .models import Review, Favourite

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_content', 'rating']
        exclude = ('profile_id', 'beer_id')

    review_content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your review (minimum 10 characters)',
        'class': 'w-full py-4 px-6 rounded-xl border-2 border-gray-200'
    }))

    rating = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Your rating 1-10',
        'class': 'w-full py-4 px-6 rounded-xl border-2 border-gray-200'
    }))

class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Favourite
        exclude = ('profile_id', 'beer_id')
