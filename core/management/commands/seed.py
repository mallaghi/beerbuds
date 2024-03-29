from django.core.management.base import BaseCommand
from marketplace.models import Beer, Store, Profile
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
    print("Clearing data")
    User.objects.filter(is_superuser=False).delete()

def create_users():
    print("Creating users")
    user = User.objects.create(
        first_name=fake.first_name_nonbinary(),
        last_name=fake.last_name(),
        username= fake.user_name(),
        email=fake.ascii_email(),
        password="tWdhsdio12",
        )
    return user


def create_profile():
    print("Creating profiles")
    user_id = User.objects.exclude(user_profile__isnull=False)
    profile = Profile.objects.create(
        user_id=random.choice(user_id),
        address=fake.address()
    )
    return profile

def create_stores():
    print("Creating stores")
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
    print("Getting random beer from API")
    punk_api_url = "https://api.sampleapis.com/beers/ale"
    response = requests.get(punk_api_url)

    if response.status_code == 200:
        beer_data = response.json()[random.randint(0, 99)]
        return beer_data
    else:
        return None

def create_beers():
    print("Creating beers")
    beer_data = get_random_beer_from_api()
    store_ids = Store.objects.all()
    stock_quantities = [100, 50, 300, 1000]
    abv = [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5]
    volume = [330.00, 355.00, 500.00, 650.00, 750.00, 1000.00, 1500.00, 2000.00, 5000.00]
    ingredients = [ 'malt', 'barely', 'gluten', 'hops', 'yeast', 'water', 'sugar', 'flavorings', 'preservatives']
    price = [5.99, 6.99, 7.99, 8.99, 9.99, 10.99, 11.99, 12.99, 13.99, 14.99]

    if beer_data:
        beer = Beer.objects.create(
            name=beer_data['name'],
            description='description ',
            stock_quantity=random.choice(stock_quantities),
            price=random.choice(price),
            store_id=random.choice(store_ids),
            beer_image=beer_data['image'],
            volume=random.choice(volume),
            abv= random.choice(abv),
            ingredients=', '.join(ingredients)
        )
        print(beer.id)
        return beer
    else:
        return None

def run_seed(self, mode):
     clear_data()
     if mode == MODE_CLEAR:
        return
     for i in range(10):
        create_users()
        create_profile()
        create_stores()
     for i in range(10):
        create_beers()
