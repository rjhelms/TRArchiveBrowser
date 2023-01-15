from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Artist, Genre, Label, Record, Style


class RecordListView(ListView):
    paginate_by = 100
    model = Record

    def prefetch_view(self, queryset):
        return queryset.prefetch_related("artist", "genres", "styles", "label", "type")

    def get_queryset(self):
        return self.prefetch_view(Record.objects)


class ArtistRecordListView(RecordListView):
    def get_queryset(self):
        self.artist = get_object_or_404(Artist, slug=self.kwargs["slug"])
        return self.prefetch_view(Record.objects.filter(artist=self.artist))


class LabelRecordListView(RecordListView):
    def get_queryset(self):
        self.label = get_object_or_404(Label, slug=self.kwargs["slug"])
        return self.prefetch_view(Record.objects.filter(label=self.label))


class GenreRecordListView(RecordListView):
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs["slug"])
        return self.prefetch_view(Record.objects.filter(genres=self.genre))


class StyleRecordListView(RecordListView):
    def get_queryset(self):
        self.style = get_object_or_404(Style, slug=self.kwargs["slug"])
        return self.prefetch_view(Record.objects.filter(styles=self.style))
