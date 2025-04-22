from django.db import models
from django.conf import settings  

class Movie(models.Model):  
    RATING_CHOICES = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    ]

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default="G")
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
