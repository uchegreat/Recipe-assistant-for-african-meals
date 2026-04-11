from rest_framework import serializers

class RecipeQuerySerializer(serializers.Serializer):
    message = serializers.CharField()
