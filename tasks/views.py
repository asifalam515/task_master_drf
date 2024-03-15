from django.shortcuts import render
from tasks.models import CreateTaskModel
from tasks.serializers import CreateTaskSerializers

from rest_framework import viewsets


class CreateTaskViewSet(viewsets.ModelViewSet):
   
    queryset = CreateTaskModel.objects.all()
    serializer_class = CreateTaskSerializers