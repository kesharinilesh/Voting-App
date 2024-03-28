from django.contrib import admin
from django.urls import include,path
from votingHome import views

app_name='votingProject'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
]