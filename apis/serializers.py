from rest_framework import serializers
from apis.models import User

class UserSerializer(serializers.Serializer):
	name = serializers.CharField(required=True,max_length=100)
	password = serializers.CharField(required=True,max_length=256)
	phone = serializers.CharField(required=True,max_length=11)
	email = serializers.CharField(required=True,max_length=100)
	role = serializers.CharField(required=True)

	def create(self,validated_data):
		return User.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name',instance.name)
		instance.password = validated_data.get('password',instance.password)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.role = validated_data.get('role', instance.role)
		instance.email = validated_data.get('email',instance.email)
		return instance


