from rest_framework import serializers

import main.models as models
import api.serializers.relations as rl

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["task"] = rl.TaskRelationsSerializer(instance.task).data
        data["category"] = rl.CategoryRelationSerializer(instance.category.all, many=True).data

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"
