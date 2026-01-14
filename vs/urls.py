from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'vs'

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
    path('chat/', views.chat, name='chat'),
    path('timer/', views.timer, name='timer'),
    path('goals/', views.goals, name='goals'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]