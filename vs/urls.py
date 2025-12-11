from django.urls import path
from . import views

app_name = 'vs'

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
]