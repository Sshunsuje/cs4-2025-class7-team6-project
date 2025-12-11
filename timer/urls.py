from django.urls import path
from . import views

app_name = 'timer'

urlpatterns = [
    path('', views.index, name='index'),
    path('save_log/', views.save_log, name='save_log'),
]