from rest_framework import serializers

from apps.clients_app.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "phone", "shop"]


class ClientReadSerializer(ClientSerializer):
    shop_id = serializers.IntegerField(source="shop.id", read_only=True)
    shop_name = serializers.CharField(source="shop.name", read_only=True)

    class Meta(ClientSerializer.Meta):
        fields = ["id", "name", "phone", "shop_id", "shop_name", "sells"]
