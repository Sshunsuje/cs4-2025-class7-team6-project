from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from timer.models import StudyLog

def index(request):
    users_with_time = User.objects.annotate(
        total_minutes=Sum('studylog__minutes')
    ).filter(total_minutes__gt=0).order_by('-total_minutes')[:10]

    ranking_data = []
    for i, user in enumerate(users_with_time, start=1):
        total = user.total_minutes
        hrs = total // 60
        mins = total % 60
        
        time_display = f"{hrs}h {mins:02d}m" if hrs > 0 else f"{mins}m"
        
        ranking_data.append({
            'rank': i,
            'username': user.username,
            'time': time_display,
        })

    return render(request, 'ranking/index.html', {'ranking_data': ranking_data})