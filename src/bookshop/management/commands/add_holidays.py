from django.core.management.base import BaseCommand
from bookshop.models import Holiday
from logging import getLogger
from ics import Calendar
from requests import get


logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.officeholidays.com/ics/ics_country.php?tbl_country=Belarus"
        calendar = Calendar(get(url).text)
        for event in calendar.events:
            h = Holiday(
                title=event.name,
                date_start=event.begin.date(),
                duration=event.duration,
                description=event.description
            )
            try:
                h.save()
                logger.warning(h.title)
            except:
                pass
