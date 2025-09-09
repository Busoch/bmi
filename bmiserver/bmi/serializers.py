from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BMIRecord

class BMISerializer(serializers.Serializer):
    weight = serializers.FloatField(min_value=1)  # kg
    height = serializers.FloatField(min_value=1)  # cm

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user
    

class BMIRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMIRecord
        fields = ["id", "weight", "height", "bmi", "category", "created_at"]
