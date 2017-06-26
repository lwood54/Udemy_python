import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProjTwo.settings')
import django
django.setup()

import random
from newApp.models import User
from faker import Faker

# call instance of fake generator
fake_generator = Faker()

# create function to populate the data
def populate(N=5):
    for entry in range(N):
        fake_first_name = fake_generator.first_name()
        fake_last_name = fake_generator.last_name()
        fake_email = fake_generator.email()

        person = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,user_email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
