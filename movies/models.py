import uuid
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название жанра')
    description = models.TextField(verbose_name='Описание жанра', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    description = models.TextField(verbose_name='Описание компании', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность фильма', help_text='Длительность в минутах')
    rental_start = models.DateField(verbose_name='Дата начала проката')
    rental_end = models.DateField(verbose_name='Дата окончания проката', blank=True, null=True)
    poster = models.ImageField(upload_to='posters', verbose_name='Постер', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='Компания', null=True, related_name='movies')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('rental_start',)


class Saloon(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название зала')
    description = models.TextField(verbose_name='Описание зала', blank=True, null=True)
    count_places = models.PositiveSmallIntegerField(verbose_name='Количество мест')
    number_of_rows = models.PositiveSmallIntegerField(verbose_name='Количество рядов')
    number_of_places = models.PositiveSmallIntegerField(verbose_name='Количество мест в ряду')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class SectorSaloon(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название сектора')
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Зал', related_name='sectors')
    # on_delete=models.CASCADE - при удалении зала, удалятся все секторы этого зала
    description = models.TextField(verbose_name='Описание сектора', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сектор зала'
        verbose_name_plural = 'Секторы залов'


class Place(models.Model):
    sector = models.ForeignKey(SectorSaloon, on_delete=models.CASCADE, verbose_name='Сектор', related_name='places')
    row_number = models.PositiveSmallIntegerField(verbose_name='Номер ряда')
    row_place = models.PositiveSmallIntegerField(verbose_name='Номер места')

    def __str__(self):
        return f'{self.sector} - {self.row_number} - {self.row_place}'
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Seanse(models.Model):
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Зал', related_name='seanses')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм', related_name='seanses')
    date = models.DateField(verbose_name='Дата сеанса')
    time = models.TimeField(verbose_name='Время сеанса')

    def __str__(self):
        return f'{self.movie} - {self.date} - {self.time}'
    
    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
        ordering = ('date', 'time')


class Ticket(models.Model):
    ticket_number = models.CharField(max_length=40, verbose_name='Номер билета', default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания билета')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления билета')
    seanse = models.ForeignKey(Seanse, on_delete=models.PROTECT, verbose_name='Сеанс', related_name='tickets')
    place = models.ForeignKey(Place, on_delete=models.PROTECT, verbose_name='Место', related_name='tickets')
    payed = models.BooleanField(verbose_name='Оплачен', default=False)
    booked = models.BooleanField(verbose_name='Забронирован', default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена билета')

    def __str__(self):
        return f'{self.ticket_number} - {self.seanse} - {self.place}'
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ('seanse', 'place')
