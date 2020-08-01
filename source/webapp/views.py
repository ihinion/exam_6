from django.shortcuts import render, redirect
from webapp.models import Entry
from webapp.forms import EntryForm


def index_view(request):
    entries = Entry.objects.filter(status='active')
    return render(request, 'index.html', {'entries': entries})


def create_view(request):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            Entry.objects.create(**form.cleaned_data)
            return redirect('index_view')
        else:
            return render(request, 'create.html', {'form': form})