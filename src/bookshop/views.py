from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from bookshop.serializer import EventSerializer, HolidaySerializer
from bookshop.models import Event, Holiday, CHOICE_DELTA
from django.db.models import Q
from logging import getLogger
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


User = get_user_model()
logger = getLogger("django")


class ListEvent(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(
            user_event=self.request.user
        )


class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def create(self, request):
        test = EventSerializer(data=request.data)
        if test.is_valid():
            test.save(user_event=request.user)
        return Response("Done")


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(
            user_event=self.request.user
        )


class GetEvents(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, date):
        date = date.split("-")
        response = Event.objects.filter(user_event=request.user)
        if len(date) == 1:
            response = response.filter(
                Q(date_stop__year=date[0])
            )
        elif len(date) == 2:
            response = response.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1])
            )
        elif len(date) == 3:
            response = response.filter(
                Q(date_stop__year=date[0]) &
                Q(date_stop__month=date[1]) &
                Q(date_stop__day=date[2])
            )
        serializer = EventSerializer(response.order_by("date_stop"), many=True)
        return Response(serializer.data)


class GetToken(APIView):
    def post(self, request):
        user = User.objects.get_or_create(
                username=request.data["username"],
                password=request.data["password"],
                email=request.data["email"],
                country=request.data["country"]
                )
        token = Token.objects.get_or_create(user=user[0])
        send_mail(
            "this is your token",
            f"token: {token[0].key}",
            "akademiynauk3@gmail.com",
            [request.data["email"]],
            fail_silently=True
        )
        return Response("please receive your token")


class ListHoliday(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = HolidaySerializer
    def get_queryset(self):
        return Holiday.objects.filter(
            country=self.request.user.country
        )
# Create your views here.
