from django.shortcuts import render


def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    return render(request, 'ranking/index.html')


def chat(request):
    return render(request, 'vs/chat.html')

def timer(request):
    return render(request, 'timer/index.html')

def goals(request):
    return render(request, 'goals/board.html')