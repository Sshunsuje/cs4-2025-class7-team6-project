from django.shortcuts import render


from django.shortcuts import render

def index(request):
    return render(request, 'vs/index.html')

def bord(request):
    return render(request, 'vs/bord.html')

from django.shortcuts import render

def index(request):
    return render(request, 'vs/index.html')

def ranking(request):
    # 【担当D】学習ランキング用
    # 本番ではデータベース(Models)から「勉強時間の合計」で降順ソートして取得します
    # 例: User.objects.order_by('-total_study_time')[:10]
    
    mock_data = [
        {'rank': 1, 'username': 'ガリ勉マスター', 'time': '42時間 15分'},
        {'rank': 2, 'username': 'テスト前の一夜漬け', 'time': '38時間 00分'},
        {'rank': 3, 'username': 'コツコツ太郎', 'time': '15時間 30分'},
        {'rank': 4, 'username': 'Team6_User', 'time': '8時間 45分'},
        {'rank': 5, 'username': '新人メンバー', 'time': '2時間 10分'},
        {'rank': 6, 'username': '新人メンバー', 'time': '2時間 09分'},
    ]

    context = {
        'ranking_data': mock_data
    }
    
    return render(request, 'vs/ranking.html', context)