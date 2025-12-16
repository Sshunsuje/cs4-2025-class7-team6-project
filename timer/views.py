# timer/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import StudyLog
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """タイマー画面を表示"""
    logs = StudyLog.objects.order_by('-created_at')[:5]
    return render(request, 'timer/index.html', {'logs': logs})

def save_log(request):
    """Ajaxで送られてきた勉強時間を保存する"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            minutes = data.get('minutes')
            
            # 【重要】0も許可するために「Noneではない」という書き方にします
            if minutes is not None:
                StudyLog.objects.create(minutes=minutes)
                return JsonResponse({'status': 'ok', 'message': f'{minutes}分を記録しました'})
            else:
                # ここが原因の可能性があります
                return JsonResponse({'status': 'error', 'message': '値が無効です'})
        except Exception as e:
            print(f"Error: {e}") # ターミナルにエラーを表示させる
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error'}, status=400)