from rest_framework import serializers
from .models import Movie, Review, Director, Genre


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = 'id title genres duration'.split()
        # exclude = 'id'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def movies_count(self, director):
        return len([movie.movie for movie in director.movies.all()])


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie

        def get_rating(self, movie):
            average_rating = sum([star.stars for star in movie.reviews.all()]) / len(
                [star.stars for star in movie.reviews.all()])
            return average_rating

        fields = '__all__'