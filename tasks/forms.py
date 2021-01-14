from django import forms
from .models import todo

class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""

        model = todo
        fields = ['title', 'complete', 'due_date']
        widget = {
            'due_date': forms.widgets.DateInput,
            'complete': forms.widgets.CheckboxInput,
            'title': forms.widgets.TextInput,
        }
