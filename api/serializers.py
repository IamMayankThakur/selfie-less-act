from rest_framework import serializers

class AddUserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=512)
	password = serializers.CharField(max_length = 512)
