from django.urls import path

from .views import enviar_sms

urlpatterns = [
    path("enviar_sms/", enviar_sms, name="enviar_sms"),
]
