from django.shortcuts import render
from tasks.models import TaskModel
from tasks.serializers import CreateTaskSerializers

from rest_framework import viewsets


class CreateTaskViewSet(viewsets.ModelViewSet):
   
    queryset = TaskModel.objects.all()
    serializer_class = CreateTaskSerializers