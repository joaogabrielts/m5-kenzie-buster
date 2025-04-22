from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from .paginators import MoviePagination

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsEmployee()]
        return [AllowAny()]
