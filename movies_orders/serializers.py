from rest_framework import serializers
from .models import MovieOrder

class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="movie.title", read_only=True)
    purchased_by = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = MovieOrder
        fields = ["id", "title", "purchased_at", "price", "purchased_by"]
        read_only_fields = ["id", "title", "purchased_at", "purchased_by"]

    def create(self, validated_data):
        movie = self.context["movie"]
        user = self.context["request"].user
        return MovieOrder.objects.create(movie=movie, user=user, **validated_data)
