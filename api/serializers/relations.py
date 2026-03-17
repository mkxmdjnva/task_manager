from rest_framework import serializers

import main.models as models

class TaskRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ("title")

class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("name", "user")