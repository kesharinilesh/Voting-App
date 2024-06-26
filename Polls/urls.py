from django.contrib import admin
from django.urls import include,path
from Polls import views
# urlpatterns = [
#     path('', views.polls, name='polls')
# ]
app_name = 'polls'
urlpatterns = [
	path('available', views.index, name ='index'),
	path('<int:question_id>/', views.detail, name ='detail'),
	path('<int:question_id>/results/', views.results, name ='results'),
	path('<int:question_id>/vote/', views.vote, name ='vote'),
]
