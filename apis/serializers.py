from rest_framework import serializers
from apis.models import User
from apis.models import Task
from apis.models import Module
from apis.models import Domain
from apis.models import Role

# class UserSerializer(serializers.Serializer):
# 	name = serializers.CharField(required=True,max_length=100)
# 	password = serializers.CharField(required=True,max_length=256)
# 	phone = serializers.CharField(required=True,max_length=11)
# 	email = serializers.CharField(required=True,max_length=100)
# 	role = serializers.CharField(required=True)

# 	def create(self,validated_data):
# 		return User.objects.create(**validated_data)

# 	def update(self,instance,validated_data):
# 		instance.name = validated_data.get('name',instance.name)
# 		instance.password = validated_data.get('password',instance.password)
# 		instance.phone = validated_data.get('phone', instance.phone)
# 		instance.role = validated_data.get('role', instance.role)
# 		instance.email = validated_data.get('email',instance.email)
# 		return instance


class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'phone', 'email', 'role')


class TaskSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = Task
        fields = ('id', 'name', 'module', 'domain',
                  'created_at', 'status', 'created_by')


class ModuleSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = Module
        fields = ('id', 'name', 'created_at', 'created_by')


class DomainSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = Domain
        fields = ('id', 'name', 'created_at', 'created_by')


class RoleSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = Role
        fields = ('id', 'name', 'created_at', 'created_by')


class PriviligeSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""
    class Meta:
        model = Role
        fields = ('id', 'name', 'created_at', 'created_by')
