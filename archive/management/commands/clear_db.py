import argparse
from csv import DictReader

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from archive import models


class Command(BaseCommand):
    help = "Deletes all record data (artists, records, labels, styles and genres"

    verbosity = 1

    def output_if_verbose(self, string):
        if self.verbosity > 0:
            self.stdout.write(string)

    def handle(self, *args, **options):
        self.verbosity = options["verbosity"]
        self.output_if_verbose("Deleting records")
        models.Record.objects.all().delete()
        self.output_if_verbose("Deleting genres")
        models.Genre.objects.all().delete()
        self.output_if_verbose("Deleting styles")
        models.Style.objects.all().delete()
        self.output_if_verbose("Deleting artists")
        models.Artist.objects.all().delete()
        self.output_if_verbose("Deleting labels")
        models.Label.objects.all().delete()
