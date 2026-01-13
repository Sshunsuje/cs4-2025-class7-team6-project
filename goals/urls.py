from django.urls import path
from . import views

app_name = "goals"

urlpatterns = [
    path("", views.board, name="board"),
    path("<int:goal_id>/done/", views.toggle_done, name="done"),
    path("<int:goal_id>/like/", views.like_goal, name="like"),
    path("<int:goal_id>/delete/", views.delete_goal, name="delete"),
]