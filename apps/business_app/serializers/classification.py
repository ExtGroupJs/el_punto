from rest_framework import serializers

from apps.business_app.models.classification import Classification


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = "__all__"
