from django.db import models

class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    hour = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='course/images')

    def __str__(self):
        return self.name