import string

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

# Create your models here.


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=4)
    return unique_slug

class NameModel(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=255)
    slug = models.SlugField(blank=True, unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slugify(self, slugify(self.name, allow_unicode=True))
        super(NameModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta: 
        abstract = True
        ordering = ['name']

class Record(models.Model):
    catalog_number = models.PositiveIntegerField(primary_key=True)
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
    title = models.CharField(null=False, blank=False, max_length=255)
    can_con = models.BooleanField(verbose_name="CanCon", default=False)
    genres = models.ManyToManyField("Genre")
    styles = models.ManyToManyField("Style", blank=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    label = models.ForeignKey("Label", blank=True, null=True, on_delete=models.PROTECT)
    type = models.ForeignKey("RecordType", on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['catalog_number']

    def __str__(self):
        return f"{self.artist} - {self.title}"

class Artist(NameModel):
    pass

class Genre(NameModel):
    pass


class Style(NameModel):
    pass


class Label(NameModel):
    pass


class RecordType(NameModel):
    pass
