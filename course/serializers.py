from rest_framework import serializers
from . models import CourseModel

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseModel
        fields = '__all__'
