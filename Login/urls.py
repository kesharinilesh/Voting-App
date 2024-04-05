from django.contrib import admin
from django.urls import include,path
from Login import views
urlpatterns = [
    path('', views.home, name='home')
]