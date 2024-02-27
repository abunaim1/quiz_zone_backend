from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="authentication/images/")

