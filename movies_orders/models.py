from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movie_orders")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_orders")
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
