from . models import Question, QuestionCategory, AnswerOption, QuestionPaper, ScriptSubmission
from rest_framework import serializers
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email')

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

class ScriptSubmissionSeriaLizer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = ScriptSubmission
        fields = '__all__'