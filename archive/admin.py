from django.contrib import admin

from .models import Artist, Genre, Label, Record, RecordType, Style


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = "catalog_number", "artist", "title", "type"
    list_display_links = "catalog_number", "title"
    list_filter = (
        "genres",
        "styles",
        "type",
    )


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Label)
admin.site.register(RecordType)
admin.site.register(Style)
