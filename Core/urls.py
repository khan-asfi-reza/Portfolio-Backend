from django.urls import path

from Core.views import MessageCreateView

urlpatterns = [
    path("message", MessageCreateView.as_view(), name="message_create")
]

