from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    return HttpResponse("This is my Voting Contact Page")