from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from bookshop.serializer import EventSerializer
from bookshop.models import Event
from django.db.models import Q


class ListEvent(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class GetEvents(APIView):
    def get(self, request, date):
        date = date.split("-")
        response = {}
        if len(date) == 1:
            response = Event.objects.filter(
                Q(date_stop__year=date[0])
            ).order_by("date_stop")
        elif len(date) == 2:
            response = Event.objects.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1])
            ).order_by("date_stop")
        elif len(date) == 3:
            response = Event.objects.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1]) &
                Q(date_stop__day=date[2])
            ).order_by("date_stop")
        serializer = EventSerializer(response, many=True)
        return Response(serializer.data)
# Create your views here.
