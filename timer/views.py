import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudyLog

def index(request):
    """タイマー画面を表示"""
    if request.user.is_authenticated:
        logs = StudyLog.objects.filter(user=request.user).order_by('-created_at')[:5]
    else:
        logs = StudyLog.objects.order_by('-created_at')[:5]
    return render(request, 'timer/index.html', {'logs': logs})

def save_log(request):
    """Ajaxで送られてきた勉強時間を保存する"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            minutes = data.get('minutes')
            
            if minutes is not None:
                # ログイン確認
                current_user = request.user if request.user.is_authenticated else None
                
                # データベースに保存
                StudyLog.objects.create(
                    user=current_user,
                    minutes=minutes
                )
                return JsonResponse({'status': 'ok', 'message': f'{minutes}分を記録しました'})
            else:
                return JsonResponse({'status': 'error', 'message': '値が無効です'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error'}, status=400)