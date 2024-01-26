from rest_framework import serializers

from .models import Movie, Company, Genre


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'description')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class GenreDetailSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Genre
            fields = ('id', 'name', 'description')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'rental_start', 'rental_end', 'company', 'genres')


class MovieDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'rental_start', 'rental_end', 'company', 'genres')
