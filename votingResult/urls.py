from django.contrib import admin
from django.urls import include,path
from votingResult import views
urlpatterns = [
    path('', views.result, name='result')
]