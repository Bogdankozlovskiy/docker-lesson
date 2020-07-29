from django.db import models
from logging import getLogger
from datetime import timedelta
from django.contrib.auth.models import User


logger = getLogger("django")
CHOICE_DELTA = [
        (timedelta(hours=1),   "За час",),
        (timedelta(hours=2), "За 2 часа"),
        (timedelta(hours=4), "За 4 часа"),
        (timedelta(days=1),    "За день"),
        (timedelta(weeks=1), "За неделю"),
]


class Event(models.Model):
    class Meta:
        verbose_name_plural = "события"
        verbose_name = "событие"
        db_table = "my_event"

    choice_delta = CHOICE_DELTA
    user_event = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="чье событие"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="название события"
    )
    date_start = models.DateTimeField(
        verbose_name="начало события"
    )
    date_stop = models.DateTimeField(
        verbose_name="окончание события",
        blank=True,
        null=True
    )
    reminder = models.DurationField(
        verbose_name="напомнить за...",
        choices=choice_delta
    )
    need_remind = models.BooleanField(
        verbose_name="Напомнить?",
        default=False
    )

    @property
    def reminder4api(self):
        for i in self.choice_delta:
            if self.reminder == i[0]:
                return i[1]
        return "not found"

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.date_stop is None:
            self.date_stop = self.date_start.replace(
                hour=23,
                minute=59,
                second=59
            )
        super().save(**kwargs)


class Holiday(models.Model):
    class Meta:
        verbose_name = "праздник"
        verbose_name_plural = "праздники"

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="название праздника"
    )
    date_start = models.DateTimeField(
        verbose_name="дата начала праздника"
    )
    duration = models.DurationField(
        verbose_name="длительность праздника"
    )
    description = models.TextField(
        verbose_name="описание праздника"
    )

    def __str__(self):
        return self.title
