# Importing necessary functions for handling HTTP requests and responses
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return (HttpResponse("Franco says Hello!"))