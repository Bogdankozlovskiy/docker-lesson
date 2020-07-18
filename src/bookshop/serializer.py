from bookshop.models import Event
from rest_framework.serializers import ModelSerializer


class ListEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "date_start", "date_stop", "reminder4api")


class CreateEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ("title", "date_start", "date_stop", "tmp_duration_field")
