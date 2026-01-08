from django.shortcuts import render, redirect
from .models import Message

def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    return render(request, 'ranking/index.html')

def timer(request):
    return render(request, 'timer/index.html')

def goals(request):
    return render(request, 'goals/board.html')


##以下日記機能の一部
def chat(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # name属性があれば適宜追加してください
            Message.objects.create(content=content)
        return redirect('vs:chat')

    messages = Message.objects.order_by('created_at')
    return render(request, 'vs/chat.html', {
        'messages': messages
    })

# --- 追加: 編集機能 ---
def edit_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message.content = content
            message.save()
    return redirect('vs:chat')

# --- 追加: 削除機能 ---
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect('vs:chat')
