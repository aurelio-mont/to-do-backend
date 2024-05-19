from rest_framework import serializers
from .models import Task     # import the Task model

# create a serializer class
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'complete', 'created')
        read_only_fields = ('id', 'created')
        