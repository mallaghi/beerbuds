from django.db import models
from marketplace.models import Profile, Beer
from django.core.validators import MinLengthValidator

# Create your models here.
class Favourite(models.Model):
    profile_id = models.ForeignKey(Profile, related_name='user_favourite', on_delete=models.CASCADE)
    beer_id = models.ForeignKey(Beer, related_name='beer_favourite', on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_id.user_id.username + " loves " + self.beer_id.name


class Review(models.Model):
    profile_id = models.ForeignKey(Profile, related_name='user_review', on_delete=models.CASCADE)
    beer_id = models.ForeignKey(Beer, related_name='beer_review', on_delete=models.CASCADE)
    review_content = models.TextField(validators=[ MinLengthValidator(50, 'Please enter a description of at least 50 characters')])
    rating = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.profile_id.user_id.username + " reviewed " + self.beer_id.name
