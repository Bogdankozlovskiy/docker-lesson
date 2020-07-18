from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from bookshop.serializer import (
    ListEventSerializer,
    CreateEventSerializer
)
from bookshop.models import Event


class ListEvent(ListAPIView):
    serializer_class = ListEventSerializer
    queryset = Event.objects.all()


class CreateEvent(CreateAPIView):
    serializer_class = CreateEventSerializer


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateEventSerializer
    queryset = Event.objects.all()
# Create your views here.
