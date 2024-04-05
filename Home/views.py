from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'homepage.html')
    