# reviews/serializers.py
from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')  # Add more fields as needed

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user