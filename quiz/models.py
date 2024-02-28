from django.db import models
from django.contrib.auth.models import User
from question.models import QuestionPaper
from rating.models import Rating
# Create your models here.


class QuizCategory(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.category
    
class Quiz(models.Model):
    quiz_category = models.ManyToManyField(QuizCategory)
    question_paper = models.ManyToManyField(QuestionPaper)
    quiz_description = models.TextField(null=True, blank=True)
