from django.contrib import admin
from django.urls import include,path
from Polls import views
urlpatterns = [
    path('', views.website, name='website')
]