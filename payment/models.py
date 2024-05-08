from django.db import models


class CheckOut(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)