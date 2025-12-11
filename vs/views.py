from django.shortcuts import render


from django.shortcuts import render

def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    return render(request, 'vs/ranking.html')



def chat(request):
    return render(request, 'vs/chat.html')

