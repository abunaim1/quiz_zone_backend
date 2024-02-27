from django.contrib import admin
from . models import QuestionCategory, AnswerOption, Question, QuestionPaper, ScriptSubmission
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(QuestionCategory, CategoryAdmin)
admin.site.register(AnswerOption)
admin.site.register(Question)
admin.site.register(QuestionPaper)
admin.site.register(ScriptSubmission)
