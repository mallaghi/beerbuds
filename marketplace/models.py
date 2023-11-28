from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=255, blank=False, null=False)
    store_email = models.EmailField(blank=False, null=False)
    phone_number = models.IntegerField(blank=False)
    description = models.TextField(validators=[
            MinLengthValidator(100, 'Please enter a description of at least 100 characters')
        ])
    user_id = models.ForeignKey(User, related_name='store_owner', on_delete=models.CASCADE)


