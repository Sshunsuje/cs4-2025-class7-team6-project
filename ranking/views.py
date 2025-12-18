from django.shortcuts import render

def index(request):
    # ダミーデータ（降順）
    mock_data = [
        {'rank': 1, 'username': 'ガリ勉マスター', 'time': '42h 15m'},
        {'rank': 2, 'username': '一夜漬け王', 'time': '38h 00m'},
        {'rank': 3, 'username': 'コツコツ太郎', 'time': '15h 30m'},
    ]
    return render(request, 'ranking/index.html', {'ranking_data': mock_data})