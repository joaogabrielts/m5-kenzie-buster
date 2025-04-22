from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "duration", "rating", "synopsis", "added_by"]

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        user = self.context["request"].user
        return Movie.objects.create(**validated_data, user=user)
