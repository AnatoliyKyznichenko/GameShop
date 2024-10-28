from rest_framework import serializers
from .models import CategoryGame, Game


class CategoryGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGame
        fields = ['id', 'name']


class GameSerializer(serializers.ModelSerializer):
    category = CategoryGameSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'name', 'description', 'rating', 'quantity', 'image', 'price', 'category']
