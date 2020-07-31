from django.core.management.base import BaseCommand
from bookshop.models import Holiday, Country
from logging import getLogger
from ics import Calendar
from requests import get


logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        for country in Country.objects.all():
            self.fill_colendar_for_country(country)
            logger.warning(country.name)


    def fill_colendar_for_country(self, country):
        url = f"https://www.officeholidays.com/ics/ics_country.php?tbl_country={country.name}"
        try:
            calendar = Calendar(get(url).text)
        except:
            return None
        for event in calendar.events:
            h = Holiday(
                title=event.name,
                date_start=event.begin.date(),
                duration=event.duration,
                description=event.description,
                country=country
            )
            try:
                h.save()
            except:
                pass
