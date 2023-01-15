from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Artist, Genre, Label, Record, Style

# Create your views here.


class RecordListView(ListView):
    paginate_by = 100
    model = Record


class ArtistRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, slug=self.kwargs["slug"])
        return Record.objects.filter(artist=self.artist)


class LabelRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.label = get_object_or_404(Label, slug=self.kwargs["slug"])
        return Record.objects.filter(label=self.label)


class GenreRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs["slug"])
        return Record.objects.filter(genres=self.genre)


class StyleRecordListView(ListView):
    paginate_by = 100

    def get_queryset(self):
        self.style = get_object_or_404(Style, slug=self.kwargs["slug"])
        return Record.objects.filter(styles=self.style)
