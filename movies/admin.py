from django.contrib import admin

from .models import Genre, Company, Movie

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
    