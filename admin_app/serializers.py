from rest_framework import serializers

class PositionSerializer(serializers.Serializer):
    username = serializers.CharField()
