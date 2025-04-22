from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .models import MovieOrder
from .serializers import MovieOrderSerializer

class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data, context={"request": request, "movie": movie})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
