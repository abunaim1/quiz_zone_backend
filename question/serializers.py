from . models import Question, QuestionCategory, AnswerOption, QuestionPaper, ScriptSubmission
from rest_framework import serializers 
from authentication.serializers import UserSerializer


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
    user = UserSerializer(many=True)
    class Meta:
        model = ScriptSubmission
        fields = '__all__'

    