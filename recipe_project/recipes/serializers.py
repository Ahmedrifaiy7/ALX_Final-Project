from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    # Automatically set the user who created the recipe
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Recipe
        fields = '__all__'
