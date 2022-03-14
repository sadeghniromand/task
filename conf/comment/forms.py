from django import forms
from . import models


class CreatCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('body',)
