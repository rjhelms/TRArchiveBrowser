from django.urls import path
from .views import ArtistRecordListView, GenreRecordListView, LabelRecordListView, RecordListView, StyleRecordListView

urlpatterns = [
    path('artist/<slug>/', ArtistRecordListView.as_view(), name="artist-record-list"),
    path('genre/<slug>/', GenreRecordListView.as_view(), name="genre-record-list"),
    path('label/<slug>/', LabelRecordListView.as_view(), name="label-record-list"),
    path('style/<slug>/', StyleRecordListView.as_view(), name="style-record-list"),
    path('', RecordListView.as_view()),
]