from django.shortcuts import render, get_object_or_404

from .models import Movie, Genre


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def movies_list(request):
    template_name = 'movies/movies.html'
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'title': 'Список фильмов пример контекста',
    }
    return render(request, template_name, context)


def movie_detail(request, pk):
    template_name = 'movies/movie.html'
    movie = get_object_or_404(Movie, pk=pk)
    # movie = Movie.objects.get(pk=pk) - вариант без обработки ошибки
    context = {
        'movie': movie,
    }
    return render(request, template_name, context)


def genres_list(request):
    template_name = 'movies/genres/genre_list.html'
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, template_name, context)

def genre_detail(request, genre_pk):
    template_name = 'movies/genres/genre_detail.html'
    genre = get_object_or_404(Genre, pk=genre_pk)
    # for movie in genre.movie_set.all():
    #     print(movie.name)
    context = {
        'genre': genre,
    }
    return render(request, template_name, context)