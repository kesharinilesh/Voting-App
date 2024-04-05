from django.contrib import admin
from django.urls import include,path
from Home import views

app_name='votingProject'

urlpatterns = [
    path('', views.home, name='home'),
    path('polls', views.polls, name ='polls'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    # path('polls', views.polls, name='polls'),
]