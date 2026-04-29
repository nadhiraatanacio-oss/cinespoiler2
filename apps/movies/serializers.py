from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "created_at"]
        read_only_fields = ["id", "created_at"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Genre.objects.all(),
        source="genres"
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "release_date",
            "duration_minutes",
            "genres",
            "genre_ids",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]