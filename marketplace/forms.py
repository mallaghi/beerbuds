from django import forms
from .models import Store, CartItem, Cart

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
