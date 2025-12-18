from django.db import models
from django.conf import settings
from django.utils import timezone

class Goal(models.Model):
    # ログイン無しでも動くように null/blank 許可
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="goals",
    )

    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    # 追加機能
    is_done = models.BooleanField(default=False)
    done_at = models.DateTimeField(null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def mark_done(self):
        self.is_done = True
        self.done_at = timezone.now()

    def mark_undone(self):
        self.is_done = False
        self.done_at = None

    def __str__(self):
        return self.text







