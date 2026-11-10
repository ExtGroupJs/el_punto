from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.business_app.models.classification import Classification
from apps.business_app.serializers.classification import ClassificationSerializer
from apps.common.permissions import CommonRolePermission


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    permission_classes = [CommonRolePermission]
