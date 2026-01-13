from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from django.urls import reverse
from .models import Goal
print("LOADED goals/views.py:", __file__, flush=True)
@require_http_methods(["GET", "POST"])
def board(request):
    # status が空/未指定でも todo 扱い
    status = request.GET.get("status") or "todo"
    print(
        "BOARD HIT:",
        request.method,
        "path=", request.path,
        "GET=", dict(request.GET),
        flush=True
    )
    # ===== POST: 追加 =====
    if request.method == "POST":
        print("POST BRANCH ENTERED", flush=True)
        text = (request.POST.get("text") or "").strip()
        print("POST text:", repr(text), flush=True)
        if not text:
            messages.error(request, "空の目標は追加できません。")
            return redirect(f"{reverse('goals:board')}?status={status}")
        if len(text) > 200:
            messages.error(request, "目標は200文字以内で入力してください。")
            return redirect(f"{reverse('goals:board')}?status={status}")
        goal = Goal(text=text)
        if request.user.is_authenticated:
            goal.user = request.user
        goal.save()
        print("SAVED goal id:", goal.id, "is_done:", goal.is_done, flush=True)
        # 追加したら未完了に戻す（追加が確実に見える）
        return redirect(f"{reverse('goals:board')}?status=todo")
    # ===== GET: 一覧 =====
    qs = Goal.objects.all().order_by("-created_at")
    if status == "done":
        qs = qs.filter(is_done=True).order_by("-done_at", "-created_at")
    else:
        qs = qs.filter(is_done=False)
    return render(request, "goals/board.html", {"goals": qs, "status": status})
@require_POST
def toggle_done(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
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
    if not goal.is_done:
        messages.error(request, "未完了の目標は削除できません。")
        return redirect("goals:board")
    if goal.user and request.user.is_authenticated and goal.user != request.user:
        messages.error(request, "他人の目標は削除できません。")
        return redirect("goals:board")
    goal.delete()
    messages.success(request, "目標を削除しました。")
    return redirect("goals:board")
