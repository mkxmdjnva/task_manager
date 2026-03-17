from rest_framework.viewsets import ModelViewSet

import main.models as models
import api.serializers as serializer

class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer