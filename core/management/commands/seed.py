from django.core.management.base import BaseCommand
from marketplace.models import Beer, Store
from django.contrib.auth.models import User
import random
from faker import Faker
import requests

fake = Faker()


# python manage.py seed --mode=refresh

""" Clear all data and creates new beers and stores """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")


    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    """Deletes all users that are not superusers"""
    User.objects.filter(is_superuser=False).delete()

def create_users():
    user = User.objects.create(
        first_name=fake.first_name_nonbinary(),
        last_name=fake.last_name(),
        username= fake.user_name(),
        email=fake.ascii_email(),
        password="tWdhsdio12",
        )
    return user

def create_stores():
    store_names = [
        "Brew Haven",
        "Hop Junction",
        "Crafted Cheers",
        "Suds Sanctuary",
        "Malt Oasis",
        "Frothy Bliss",
        "Barrel & Bubbles",
        "Hoppy Hideaway",
        "Ale Alcove",
        "Pint Paradise",
        "Lager Lounge",
        "Bubbly Nook",
        "Crafty Quench",
        "Hop Harmony",
        "Brews & Bites",
        "Froth Frontier",
        "Sip & Soothe",
        "Mosaic Drafts",
        "Tap Trail",
        "Barrel Boulevard"
]
    descriptions = [
        "Crafty brews, cozy ambiance. Your go-to for a sip of joy!",
        "Hoppy delights await! Discover the essence of beer bliss.",
        "Savor the flavor! A beer haven with a dash of excitement.",
        "Brews that speak volumes. Unleash your inner beer enthusiast.",
        "Cheers to variety! A beer emporium for every palate.",
        "Quench your thirst for quality. Dive into beer paradise.",
        "Where hops meet happiness. A journey of beer discovery.",
        "Pouring perfection since day one. Your beer destination.",
        "Crafted with care, served with flair. Beer magic in every sip.",
        "Brews that tell a story. Embrace the taste of tradition.",
        "Raise your glass to excellence. A symphony of beer flavors.",
        "Bubbles of joy in every bottle. Explore the beer mosaic.",
        "From malts to moments. Your beer sanctuary awaits.",
        "Brewtiful choices, brewed to perfection. Dive in, savor life.",
        "A tapestry of tastes. Where every beer is a masterpiece.",
        "Hop-forward, flavor-packed. Beer brilliance in every drop.",
        "Brewed for joy, served with a smile. Your happy place awaits.",
        "Sip, savor, repeat. An endless journey of beer delight.",
        "A blend of hops and happiness. Your passport to beer bliss.",
        "Crafted with passion, poured with precision. Cheers to joy!",
        "Brewing dreams, one pint at a time. Your beer haven beckons.",
        "Bold flavors, cozy vibes. Your escape to beer paradise.",
        "Sip-worthy selections, served with a side of smiles.",
        "From taps to tales. Discover the magic within each pour.",
        "Where beer meets brilliance. Quench your curiosity here."
]

    user_id =User.objects.exclude(store__isnull=False)


    store = Store.objects.create(
        store_name=random.choice(store_names),
        store_email= fake.ascii_company_email(),
        phone_number= fake.phone_number(),
        description=random.choice(descriptions),
        user_id=random.choice(user_id)
    )

    return store

def get_random_beer_from_api():
    punk_api_url = "https://api.punkapi.com/v2/beers/random"
    response = requests.get(punk_api_url)

    if response.status_code == 200:
        beer_data = response.json()[0]
        return beer_data
    else:
        return None

def create_beers():
    beer_data = get_random_beer_from_api()
    store_ids = Store.objects.all()
    stock_quantities = [100, 50, 300, 1000]
    prices = [4.99, 5.99, 6.99, 7.99, 8.99, 9.99]

    if beer_data:
        beer = Beer.objects.create(
            name=beer_data['name'],
            description=beer_data['description'],
            stock_quantity=random.choice(stock_quantities),
            price=random.choice(prices),
            store_id=random.choice(store_ids),
            beer_image=beer_data['image_url'],
            volume=beer_data['volume']['value'],
            abv=beer_data['abv'],
            ingredients= beer_data['ingredients']['malt'][0]['name'],
        )
        return beer
    else:
        return None

def run_seed(self, mode):
     clear_data()
     if mode == MODE_CLEAR:
        return
     for i in range(10):
        create_users()
        create_stores()
     for i in range(100):
        create_beers()
