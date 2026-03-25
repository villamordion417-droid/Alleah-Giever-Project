from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Optional title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your thoughts here...', 'rows': 10}),
        }