from django.shortcuts import render
from django.http import JsonResponse
from .models import StudyLog
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """タイマー画面を表示"""
    # 過去の履歴を新しい順に5件取得して表示する
    logs = StudyLog.objects.order_by('-created_at')[:5]
    return render(request, 'timer/index.html', {'logs': logs})

def save_log(request):
    """Ajaxで送られてきた勉強時間を保存する"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            minutes = data.get('minutes')
            
            if minutes and minutes > 0:
                StudyLog.objects.create(minutes=minutes)
                return JsonResponse({'status': 'ok', 'message': f'{minutes}分を記録しました'})
            else:
                return JsonResponse({'status': 'error', 'message': '1分未満は記録されません'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error'}, status=400)