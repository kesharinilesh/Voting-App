from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def website(request):
    return HttpResponse("This is my Voting Website Page")