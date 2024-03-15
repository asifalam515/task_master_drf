from tasks.models import TaskModel
from rest_framework import serializers

class CreateTaskSerializers(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = TaskModel
        fields ='__all__'