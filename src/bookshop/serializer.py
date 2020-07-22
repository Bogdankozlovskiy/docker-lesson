from bookshop.models import Event, CHOICE_DELTA
from rest_framework.serializers import ModelSerializer,  CharField
from logging import getLogger


logger = getLogger("django")


class EventSerializer(ModelSerializer):
    tmp_duration = CharField(source="reminder4api")

    class Meta:
        model = Event
        fields = ("title", "date_start", "date_stop", "tmp_duration")

    def save(self, *args, **kwargs):
        # logger.warning(str(self.validated_data))
        for item in CHOICE_DELTA:
            if self.validated_data["reminder4api"] == item[1]:
                self.validated_data["reminder"] = item[0]
        del self.validated_data["reminder4api"]
        super().save(*args, **kwargs)
