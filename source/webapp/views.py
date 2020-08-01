from django.shortcuts import render
from webapp.models import Entry


def index_view(request):
    entries = Entry.objects.filter(status='active')
    return render(request, 'index.html', {'entries': entries})
