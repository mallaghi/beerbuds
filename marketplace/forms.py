from django import forms
from .models import Store, Beer

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name", 'store_email', 'phone_number', 'description']
        exclude = ('user_id',)


class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'description', 'stock_quantity', 'price',
                   'beer_image', 'volume', 'abv', 'ingredients']
        exclude = ('store_id',)
