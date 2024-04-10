from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.

class CourseViewset(viewsets.ModelViewSet):
    queryset = models.CourseModel.objects.all()
    serializer_class = serializers.CourseSerializers