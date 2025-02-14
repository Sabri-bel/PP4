from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    form class for add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
