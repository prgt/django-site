#from django.shortcuts import render
from django.http import HttpResponse

def test (request):
    return HttpResponse("Test page!")

def index (request):
    return HttpResponse("It's my project!")

def page1 (request):
    return HttpResponse("Page1!")

# Create your views here.
