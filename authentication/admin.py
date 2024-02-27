from django.contrib import admin
from . import models
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz']
        
    def user(self, obj):
        return obj.user.first_name
    def quiz(self, obj):
        return obj.quiz.name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        

    
admin.site.register(models.Participant, ParticipantAdmin)
admin.site.register(models.UserImage)