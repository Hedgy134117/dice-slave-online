from django import forms
from . import models

class CreateSheet(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = '__all__'