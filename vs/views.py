from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    return render(request, 'ranking/index.html')


def chat(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
        return redirect('vs:chat')

    messages = Message.objects.order_by('created_at')
    return render(request, 'vs/chat.html', {
        'messages': messages
    })

def timer(request):
    return render(request, 'timer/index.html')

def goals(request):
    return render(request, 'goals/board.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
