import random
from faker import Faker
from django.utils import timezone
from books_app.models import Author, Books, Publisher, User
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')

django.setup()
fake = Faker()

def generate_fake_data():
    # Generate Users
    users = [User(username=fake.user_name(), email=fake.email()) for _ in range(20)]
    User.objects.bulk_create(users)

    # Generate Authors
    authors = [
        Author(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            address=fake.address(),
            zipcode=fake.random_int(min=10000, max=99999),
            telephone=fake.phone_number(),
            joindate=fake.date_this_decade(),
            popularity_score=fake.random_int(min=1, max=10),
        )
        for _ in range(10)
    ]
    Author.objects.bulk_create(authors)

    # Generate Publishers
    publishers = [
        Publisher(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            joindate=fake.date_this_decade(),
            popularity_score=fake.random_int(min=1, max=10),
        )
        for _ in range(5)
    ]
    Publisher.objects.bulk_create(publishers)

    # Generate Books
    books = [
        Books(
            title=fake.text(max_nb_chars=50),
            genre=fake.word(),
            price=fake.random_int(min=10, max=100),
            published_date=timezone.now(),
            author=random.choice(authors),
            publisher=random.choice(publishers),
        )
        for _ in range(30)
    ]
    Books.objects.bulk_create(books)

    # Add followers for authors
    for author in authors:
        followers = random.sample(users, k=fake.random_int(min=1, max=10))
        author.followers.set(followers)

    print('Fake data with followers generated successfully.')

# Call the function to generate and insert fake data
generate_fake_data()
