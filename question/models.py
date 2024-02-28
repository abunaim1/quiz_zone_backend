from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DIFFICULTY = [
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
]

class QuestionCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.name
    

class QuestionPaper(models.Model):
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50, choices = DIFFICULTY)
    mark = models.IntegerField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=100)
    mark = models.IntegerField()
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE, null=True, blank=True)

class AnswerOption(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, null=True, blank=True)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    
class ScriptSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mark = models.IntegerField()