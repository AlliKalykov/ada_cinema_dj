from django.urls import path

from .views import index, movies_list, movie_detail, genres_list, genre_detail

urlpatterns = [
    path('', index),
    path('list', movies_list),
    path('detail/<int:pk>', movie_detail),
    path('genres', genres_list),
    path('genres/<int:genre_pk>', genre_detail),
]