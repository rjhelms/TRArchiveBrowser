from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Record

# Create your views here.

class RecordListView(ListView):
    model = Record

def index(request):
    return HttpResponse("Hello, world. You're at the archive index.")
