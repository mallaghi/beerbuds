from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name", 'store_email', 'phone_number', 'description']
        exclude = ('user_id',)
