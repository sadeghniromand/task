from django import forms
from . import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
