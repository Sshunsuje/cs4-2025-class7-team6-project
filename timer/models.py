from django.db import models

# Create your models here.

# timer/models.py

from django.db import models

class StudyLog(models.Model):
    minutes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M')} - {self.minutes}分"