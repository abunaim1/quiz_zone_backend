from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.

class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer