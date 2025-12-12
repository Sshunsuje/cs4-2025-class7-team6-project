from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from .models import Goal
@require_http_methods(["GET", "POST"])
def board(request):
    # フィルタ（statusだけ残す）
    status = request.GET.get("status", "todo")  # todo / done
    if request.method == "POST":
        text = (request.POST.get("text") or "").strip()
        if not text:
            messages.error(request, "空の目標は追加できません。")
            return redirect("goals:board")
        if len(text) > 200:
            messages.error(request, "目標は200文字以内で入力してください。")
            return redirect("goals:board")
        goal = Goal(text=text)
        # ログインしてたら user 紐付け
        if request.user.is_authenticated:
            goal.user = request.user
        goal.save()
        return redirect("goals:board")
    # 一覧取得
    qs = Goal.objects.all().order_by("-created_at")
    if status == "done":
        qs = qs.filter(is_done=True).order_by("-done_at", "-created_at")
    else:
        qs = qs.filter(is_done=False)
    context = {
        "goals": qs,
        "status": status,
    }
    return render(request, "goals/board.html", context)
@require_POST
def toggle_done(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    # 「自分の目標だけ完了できる」制御（ログインしてる場合のみ厳格に）
    if goal.user and request.user.is_authenticated and goal.user != request.user:
        messages.error(request, "他人の目標は操作できません。")
        return redirect("goals:board")
    if goal.is_done:
        goal.mark_undone()
    else:
        goal.mark_done()
    goal.save()
    return redirect(request.META.get("HTTP_REFERER", "goals:board"))
@require_POST
def like_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    goal.likes += 1
    goal.save()
    return redirect(request.META.get("HTTP_REFERER", "goals:board"))

@require_POST
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)

    # 完了済み以外は削除させない
    if not goal.is_done:
        messages.error(request, "未完了の目標は削除できません。")
        return redirect("goals:board")

    # 他人の目標を削除できないように（ログイン時）
    if goal.user and request.user.is_authenticated and goal.user != request.user:
        messages.error(request, "他人の目標は削除できません。")
        return redirect("goals:board")

    goal.delete()
    messages.success(request, "目標を削除しました。")
    return redirect("goals:board")















