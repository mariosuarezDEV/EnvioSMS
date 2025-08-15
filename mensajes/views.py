from django.shortcuts import render, HttpResponse
from sms import send_sms

# Create your views here.


def enviar_sms(request):
    send_sms(
        "Hola desde django!",
        "+19124754305",
        ["+522282578460"],
        fail_silently=False,
    )
    return HttpResponse("SMS enviado!")
