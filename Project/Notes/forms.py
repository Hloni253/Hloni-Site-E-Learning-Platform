from django import forms
from .models import Notes, Comment


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["name","topic","status","notes"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
