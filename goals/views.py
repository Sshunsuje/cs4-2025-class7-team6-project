from django.shortcuts import render
from .models import Goal

def board(request):
    goals = Goal.objects.order_by('-created_at')
    return render(request, 'goals/board.html', {'goals': goals})