from django.db import models
from question.models import QuestionPaper
from django.contrib.auth.models import User
# Create your models here.

RATING = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐⭐'),
]

class Rating (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.CharField(max_length = 50, choices=RATING)
    feedback = models.TextField()

    def __str__(self):
        return f'Rating for {self.quiz} by {self.user}'