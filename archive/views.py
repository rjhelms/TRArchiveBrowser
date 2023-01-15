from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Artist, Genre, Label, Record, Style

# Create your views here.


class RecordListView(ListView):
    paginate_by = 100
    model = Record

    def get_queryset(self):
        return Record.objects.prefetch_related('artist', 'genres', 'styles', 'label', 'type')

class ArtistRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, slug=self.kwargs["slug"])
        return Record.objects.filter(artist=self.artist).prefetch_related('artist', 'genres', 'styles', 'label', 'type')


class LabelRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.label = get_object_or_404(Label, slug=self.kwargs["slug"])
        return Record.objects.filter(label=self.label).prefetch_related('artist', 'genres', 'styles', 'label', 'type')


class GenreRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs["slug"])
        return Record.objects.filter(genres=self.genre).prefetch_related('artist', 'genres', 'styles', 'label', 'type')


class StyleRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.style = get_object_or_404(Style, slug=self.kwargs["slug"])
        return Record.objects.filter(styles=self.style).prefetch_related('artist', 'genres', 'styles', 'label', 'type')
