from django import forms
from .models import Store, Beer

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name", 'store_email', 'phone_number', 'description']
        exclude = ('user_id',)


class BeerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Beer here'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Show the customer some information about the beer'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Hops, yeast, malted grains, water...'}))

    class Meta:
        model = Beer
        fields = ['name', 'description', 'stock_quantity', 'price',
                   'beer_image', 'volume', 'abv', 'ingredients']
        exclude = ('store_id',)
