from . models import Question, QuestionCategory, AnswerOption, QuestionPaper, ScriptSubmission
from rest_framework import serializers 


class QuestionSerializer(serializers.ModelSerializer):
    question_paper_name = serializers.CharField(source='question_paper.name', read_only=True)
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
    question_category_name = serializers.CharField(source='question_category.name', read_only=True)
    class Meta:
        model = QuestionPaper
        fields = '__all__'

class ScriptSubmissionSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = ScriptSubmission
        fields = '__all__'

    