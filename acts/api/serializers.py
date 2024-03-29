from rest_framework import serializers

class AddUserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=512)
	password = serializers.CharField(max_length = 512)
	

class AddCategorySerializer(serializers.Serializer):
	category_name = serializers.CharField(max_length=512)


class GetCategoryActResponseSerializer(serializers.Serializer):
	actId = serializers.IntegerField()
	username = serializers.CharField()
	timestamp = serializers.DateTimeField()
	caption = serializers.CharField()
	upvotes = serializers.IntegerField()
	imgb64 = serializers.CharField()
