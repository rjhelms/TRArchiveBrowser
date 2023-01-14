import argparse
from csv import DictReader

from django.core.management.base import BaseCommand, CommandError

from archive import models


class Command(BaseCommand):
    help = "Import a csv file of records"

    def add_arguments(self, parser):
        parser.add_argument(
            "input_file",
            nargs=1,
            type=argparse.FileType("r", encoding="utf8"),
            help="CSV file to be imported",
        )
        parser.add_argument(
            "recordtype",
            nargs=1,
            type=int,
            help="Database ID of record type for import",
        )

    def handle(self, *args, **options):
        csv_data = DictReader(options["input_file"][0])
        for row in csv_data:
            artist, artist_created = models.Artist.objects.get_or_create(
                name=row["Artist"].strip()
            )
            if artist_created:
                self.stdout.write(f"Created artist {artist}")
            record, record_created = models.Record.objects.get_or_create(
                catalog_number=row["Cat #"],
                defaults={"artist": artist, "type_id": options["recordtype"][0]},
            )
            record.title = row["Album"].strip()
            if row["CanCon"].strip().lower() == "cancon":
                record.can_con = True
            if row["Genre(s)"]:
                for genre_name in [x.strip() for x in row["Genre(s)"].split(",")]:
                    genre, genre_created = models.Genre.objects.get_or_create(
                        name=genre_name
                    )
                    record.genres.add(genre)
                    if genre_created:
                        self.stdout.write(f"Created genre {genre}")
            if row["Style(s)"]:
                for style_name in [x.strip() for x in row["Style(s)"].split(",")]:
                    style, style_created = models.Style.objects.get_or_create(
                        name=style_name
                    )
                    record.styles.add(style)
                    if style_created:
                        self.stdout.write(f"Created style {style}")
            if row["Label"]:
                label, label_created = models.Label.objects.get_or_create(
                    name=row["Label"].strip()
                )
                record.label = label
                if label_created:
                    self.stdout.write(f"Created label {label}")
            if (
                row["Original Year of Release"]
                and row["Original Year of Release"] != "Unknown"
            ):
                record.release_year = int(row["Original Year of Release"])
            record.save()
            if record_created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created record {record.catalog_number}: {record.artist} - {record.title}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated record {record.catalog_number}: {record.artist} - {record.title}"
                    )
                )
