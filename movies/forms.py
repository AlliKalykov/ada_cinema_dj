from django.forms import ModelForm

from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'duration', 'rental_start', 'rental_end', 'poster', 'company', 'genres')

    
