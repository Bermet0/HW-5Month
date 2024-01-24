from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import ReviewSerializer, DirectorSerializer, MovieSerializer


@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_detail(request, id):
    director = Director.objects.get(id=id)
    data = {'director': {
        'name': director.name,
    }}
    return Response(data=data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    data = {'movie': {
        'title': movie.title,
        'description': movie.description,
        'duration': movie.duration,
        'director': movie.director.name,
    }}
    return Response(data=data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def review_detail(request, id):
    review = Review.objects.get(id=id)
    data = {'review': {
        'text': review.text,
        'movie': review.movie.title,
    }}
    return Response(data=data)
