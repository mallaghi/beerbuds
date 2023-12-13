from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["store_name", 'store_email', 'phone_number', 'description']
        exclude = ('user_id',)


#     business_email = forms.EmailField()
#     phone_number = forms.CharField(max_length=15)
#     description = forms.CharField(widget=forms.Textarea)
#     user_id = forms.ModelChoiceField(queryset=User.objects.)
