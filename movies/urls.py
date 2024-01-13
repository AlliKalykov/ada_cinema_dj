from django.urls import path

from .views import index, movies_list, movie_detail, genres_list, genre_detail, SeanseGenericView, SeanseDetailView, MovieCreateView

urlpatterns = [
    path('', index),
    path('list', movies_list),
    path('detail/<int:pk>', movie_detail),
    path('create', MovieCreateView.as_view()),
    path('genres', genres_list),
    path('genres/<int:genre_pk>', genre_detail),
    path('seanses', SeanseGenericView.as_view()),
    path('seanses/<int:pk>', SeanseDetailView.as_view()),
]