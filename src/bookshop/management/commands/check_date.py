from django.core.management.base import BaseCommand
from bookshop.models import Event
from logging import getLogger
from datetime import datetime
from django.core.mail import send_mail


logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        datetime.now()
        logger.warning("works")
