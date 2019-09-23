from django import forms
from . import models

class CreateSheet(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = '__all__'

# class CreateAttack(forms.ModelForm):
#     class Meta:
#         model = models.Attack
#         fields = '__all__'