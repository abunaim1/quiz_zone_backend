from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models, serializers
# Create your views here.


class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.QuestionCategory.objects.all()
    serializer_class = serializers.QuestionCategorySerializer

class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset = models.QuestionPaper.objects.all()
    serializer_class = serializers.QuestionPaperSerializer

class QuestionPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    pagination_class = QuestionPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class AnswerOptionViewset(viewsets.ModelViewSet):
    queryset = models.AnswerOption.objects.all()
    serializer_class = serializers.AnswerOptionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        question = self.request.query_params.get("question")
        if question:
            queryset = queryset.filter(question=question)
        return queryset