from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.title