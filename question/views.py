from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models, serializers
from urllib.parse import urlparse
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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
    pagination_class =  QuestionPagination

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
    
class ScriptSubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.ScriptSubmission.objects.all()
    serializer_class = serializers.ScriptSubmissionSeriaLizer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = self.queryset.filter(id=user_id)
            return queryset
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            print(data.user.email)
            email_subject = 'You Script Marks'
            email_body = render_to_string('script_mail.html', {'mark': data.mark, 'username':data.user.username, 'email':data.user.email})
            email = EmailMultiAlternatives(email_subject, '', to=[data.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check Your Mail To Know Your Marks")
        return Response(serializer.data)

