from django.shortcuts import render
from .models import Message

def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    return render(request, 'vs/ranking.html')

def ranking(request):
    return render(request, 'vs/bord.html')


def bord(request):
    return render(request, 'vs/bord.html')

from django.shortcuts import render, redirect
from .models import Message

def chat(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
        return redirect('chat')

    messages = Message.objects.order_by('created_at')
    return render(request, 'vs/chat.html', {
        'messages': messages
    })
