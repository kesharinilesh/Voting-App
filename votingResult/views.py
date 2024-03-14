from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def result(request):
    return HttpResponse("This is my Voting Result Page")