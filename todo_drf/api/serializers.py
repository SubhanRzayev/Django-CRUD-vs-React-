from django.db.models import fields
from rest_framework import serializers

from todo_drf.models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
        



