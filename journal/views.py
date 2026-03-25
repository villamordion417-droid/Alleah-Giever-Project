from django.shortcuts import render, redirect
from .models import JournalEntry
from .forms import JournalEntryForm

def home(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'journal/home.html', {'entries': entries})

def create_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/create.html', {'form': form})
