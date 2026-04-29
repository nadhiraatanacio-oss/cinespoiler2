from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "release_date", "duration_minutes", "is_active"]
    search_fields = ["title"]
    list_filter = ["is_active", "genres"]
    filter_horizontal = ["genres"]