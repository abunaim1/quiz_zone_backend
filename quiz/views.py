from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import models, serializers

# Create your views here.

class QuizCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.QuizCategory.objects.all()
    serializer_class = serializers.QuizCategorySerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get("category_slug")
        if category_slug:
            for quiz in queryset:
                for cat in quiz.quiz_category.all():
                    if cat.category==category_slug:
                        category_slug = cat.id
                        queryset = queryset.filter(quiz_category=category_slug)
        return queryset
        