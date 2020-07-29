from django.core.management.base import BaseCommand
from bookshop.models import Event
from logging import getLogger
from datetime import datetime
from django.core.mail import send_mail
import pytz


utc = pytz.UTC
logger = getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = utc.localize(datetime.now())
        all_events = Event.objects.all()
        for event in all_events:
            if event.need_remind and event.date_start - event.reminder <= now:
                email = event.user_event.email
                send_mail(
                    "holiday remainder",
                    f"{event.title} - {event.date_start}",
                    "akademiynauk3@gmail.com",
                    [email],
                    fail_silently=True
                )
                event.need_remind = False
                event.save()
                logger.warning("sent")
