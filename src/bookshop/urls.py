from django.urls import path
from bookshop import views


urlpatterns = [
    path("listEvent/", views.ListEvent.as_view()),
    path("CreateEvent/", views.CreateEvent.as_view()),
    path("RUDEvent/<int:pk>/", views.RetrieveUpdateDestroy.as_view()),
    path("get/<str:date>/", views.GetEvents.as_view())
]