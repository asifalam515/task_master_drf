from tasks.models import CreateTaskModel
from rest_framework import serializers

class CreateTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateTaskModel
        fields ='__all__'