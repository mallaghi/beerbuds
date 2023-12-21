from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_content', 'rating', 'beer_id']
        exclude = ('profile_id', 'beer_id')
