from django.core.management.base import BaseCommand
from bookshop.models import Country
from logging import getLogger
from bs4 import BeautifulSoup
from requests import get


logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
    	url = "https://www.officeholidays.com/countries"
    	soup = BeautifulSoup(get(url).text)
    	for column in soup.find_all("div", {"class":"four omega columns"}):
    		for country in column.find_all("a"):
    			country = country.text[2:]
    			Country.objects.create(name=country)
    			logger.warning(f"{country} has been added")