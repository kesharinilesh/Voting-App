from django.contrib import admin
from django.urls import include,path
from Contact import views
urlpatterns = [
    path('', views.contact, name='contact')
]