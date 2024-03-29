from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=255, blank=False, null=False)
    store_email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(blank=False, max_length=13)
    description = models.TextField(validators=[
            MinLengthValidator(100, 'Please enter a description of at least 100 characters')
        ])
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    class Meta:
        ordering=['store_name']

class Profile(models.Model):
    user_id = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=350)

    def __str__(self):
        return self.user_id.username


class Beer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
<<<<<<< HEAD
    description = models.TextField(blank=False, validators=[ MinLengthValidator(5, 'Please enter a description of at least 50 characters')])
    stock_quantity = models.IntegerField(blank=False, null=False, default=100)
=======
    description = models.TextField(blank=False, validators=[ MinLengthValidator(50, 'Please enter a description of at least 50 characters')])
    stock_quantity = models.IntegerField(blank=False, null=False)
>>>>>>> e54aa33bc5cb2f8d2f7e340a5357fd3e5154f25e
    price = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)
    store_id = models.ForeignKey(Store, related_name='beer_store', on_delete=models.CASCADE)
    beer_image = models.ImageField(upload_to='beer_images', blank=False, null=False)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    abv = models.DecimalField(max_digits=6, decimal_places=1)
    ingredients = models.TextField(validators=[ MinLengthValidator(50, 'Please enter a description of at least 50 characters')])

    def __str__(self):
        return self.name
<<<<<<< HEAD
=======

>>>>>>> e54aa33bc5cb2f8d2f7e340a5357fd3e5154f25e
class OrderItem(models.Model):
    beer_id = models.ForeignKey(Beer, related_name='beer_order', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    def __str__(self):
        return self.beer_id.name + str(self.quantity)


class Order(models.Model):
    profile_id = models.ForeignKey(Profile, related_name='user_order', on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)
    order_items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    beer_id = models.ForeignKey(Beer, related_name='beer_cart', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return self.beer_id.name + str(self.quantity)


class Cart(models.Model):
    profile_id = models.ForeignKey(Profile, related_name='user_cart', on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)

    def calculate_total_price(self):
        total_price = sum((item.beer_id.price * item.quantity) if item.beer_id else 0 for item in self.cart_items.all())
        self.total_price = total_price
        self.save()
