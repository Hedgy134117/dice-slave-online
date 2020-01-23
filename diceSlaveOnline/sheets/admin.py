from django.contrib import admin
from .models import Sheet, SheetGroup, Item, Skill, Spell

# Register your models here.
admin.site.register(Skill)
admin.site.register(Item)
admin.site.register(Sheet)
admin.site.register(SheetGroup)
admin.site.register(Spell)