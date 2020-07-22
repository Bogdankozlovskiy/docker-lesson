from django.core.management.base import BaseCommand, CommandError
from bookshop.models import Event
from logging import getLogger
from datetime import datetime


logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        datetime.now()
        logger.warning("works")
