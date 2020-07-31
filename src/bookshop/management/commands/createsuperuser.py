from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from getpass import getpass
from bookshop.models import Country


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
    	username = input("Username: ")
    	email = input("Email: ")
    	password1 = getpass("Password: ")
    	password2 = getpass("Password(again): ")
    	if password1 != password2:
    		raise Exception("wrong password")
    	country = input("Country: ")
    	User.objects.create_superuser(
    		username=username,
    		email=email,
    		password=password1,
    		country=Country.objects.get(name=country),
    		is_superuser=True
    		)
    	print("superuser created successfully")