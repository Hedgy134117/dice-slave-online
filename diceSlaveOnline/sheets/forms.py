from django import forms
from . import models

class AddItem(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'

class CreateSheet(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = '__all__'