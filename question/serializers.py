from . models import Question, QuestionCategory, AnswerOption, QuestionPaper
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    question_paper = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = '__all__'

class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = '__all__'

class AnswerOptionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = AnswerOption
        fields = '__all__'
            
class QuestionPaperSerializer(serializers.ModelSerializer):
    question_category = serializers.StringRelatedField()
    class Meta:
        model = QuestionPaper
        fields = '__all__'
        
