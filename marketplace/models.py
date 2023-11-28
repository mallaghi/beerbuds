from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=255, blank=False, null=False)
    store_email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(blank=False, max_length=13)
    description = models.TextField(validators=[
            MinLengthValidator(100, 'Please enter a description of at least 100 characters')
        ])
    user_id = models.ForeignKey(User, related_name='store_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    class Meta:
        ordering=['store_name']

class Profile(models.Model):
    user_id = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=350)

    def __str__(self):
        return self.user_id.username
