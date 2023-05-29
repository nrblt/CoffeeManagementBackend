from rest_framework import serializers

class PositionSerializer(serializers.Serializer):
    username = serializers.CharField()

class CreateStaffAccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    position = serializers.CharField()
