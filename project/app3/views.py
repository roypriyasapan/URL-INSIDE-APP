from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("WELCOME TO MY APP 3 HOME PAGE!!!.....")
