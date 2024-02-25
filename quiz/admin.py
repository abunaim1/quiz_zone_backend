from django.contrib import admin
from . models import QuizCategory, Quiz
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Quiz)
admin.site.register(QuizCategory, CategoryAdmin)
