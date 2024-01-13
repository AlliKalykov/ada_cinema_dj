from django.contrib import admin

from .models import Genre, Company, Movie, Seanse, Saloon

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'rental_start', 'rental_end', 'company')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('company', 'genres')
    filter_horizontal = ('genres',)
    save_on_top = True
    save_as = True


@admin.register(Seanse)
class SeanseAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'saloon', 'date', 'time')
    list_display_links = ('id', 'movie')
    search_fields = ('movie',)
    list_filter = ('saloon', 'movie')
    save_on_top = True
    save_as = True
    

@admin.register(Saloon)
class SaloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count_places', 'number_of_rows', 'number_of_places')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('count_places',)
    save_on_top = True
    save_as = True