from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def salutacio(request):
    return HttpResponse("<h1>Hola món</h1>")
