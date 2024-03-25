from django import forms
from .models import Store, Beer, CartItem, Cart, OrderItem, Order

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name", 'store_email', 'phone_number', 'description']
        exclude = ('user_id',)

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        exclude = ('beer_id','profile_id')
        widgets = {
            'quantity': forms.Select(choices=[(i, str(i)) for i in range(1, 30)]),  # 30 to be changed to the beer stock quantity later
        }


class BeerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Beer here'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Show the customer some information about the beer'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Hops, yeast, malted grains, water...'}))

    class Meta:
        model = Beer
        fields = ['name', 'description', 'stock_quantity', 'price',
                   'beer_image', 'volume', 'abv', 'ingredients']
        exclude = ('store_id',)

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']
        exclude = ('beer_id','profile_id')
        widgets = {
            'quantity': forms.Select(choices=[(i, str(i)) for i in range(1, 30)]),  # 30 to be changed to the beer stock quantity later
        }
