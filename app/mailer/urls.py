from django.urls import path
from . import views

urlpatterns = [
    path("compose/", views.compose_view, name="compose"),
    path("sent/", views.sent_view, name="sent"),
]