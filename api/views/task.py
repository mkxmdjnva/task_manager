from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
)

import main.models as models
import api.serializers as serializer

class TaskListView(ListAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskSerializer


class TaskCreateView(CreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskSerializer


class TaskRetrieveView(RetrieveAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskDetailSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializer.CategorySerializer


class TaskDeleteView(DestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializer.CategorySerializer
