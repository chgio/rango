from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner! Check out the <a href='/rango/about/'>About</a> page!")

def about(request):
    return HttpResponse("Rango says here is the about page. Back to the <a href='/rango/'>Index</a>?")
