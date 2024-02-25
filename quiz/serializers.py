from rest_framework import serializers
from . import models
from question.serializers import QuestionPaperSerializer


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizCategory
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    quiz_category = serializers.StringRelatedField(many=True)
    question_paper = QuestionPaperSerializer(many=True)

    class Meta:
        model = models.Quiz
        fields = '__all__'