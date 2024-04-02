from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ["id", "Name", "Birthdate", "Score", "Grade"]