from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from webapp.forms import EntryForm, SearchForm


def index_view(request):
    form_1 = SearchForm(data=request.GET)
    form_2 = EntryForm()
    entries = Entry.objects.filter(status='active').order_by('-created_at')
    if form_1.is_valid():
        search = form_1.cleaned_data["search"]
        if search:
            entries = entries.filter(name__icontains=form_1.cleaned_data["search"])
    return render(request, 'index.html', {'entries': entries, 'form_1': form_1, 'form_2': form_2})



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


def update_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(data={
            'name': entry.name,
            'mail': entry.mail,
            'text': entry.text,
        })
        return render(request, 'update.html', context={'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.name = form.cleaned_data['name']
            entry.mail = form.cleaned_data['mail']
            entry.text = form.cleaned_data['text']
            entry.save()
            return redirect('index_view')
        else:
            return render(request, 'update.html', context={'form': form, 'entry': entry})


def delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('index_view')
    return render(request, 'delete.html', {'entry': entry})