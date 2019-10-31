from django import forms
from . import models

class AddItem(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'

class AddSpell(forms.ModelForm):
    class Meta:
        model = models.Spell
        fields = '__all__'

class CreateSheet(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = '__all__'

class CreateGroup(forms.ModelForm):
    class Meta:
        model = models.SheetGroup
        fields = '__all__'

class AddSkill(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = '__all__'