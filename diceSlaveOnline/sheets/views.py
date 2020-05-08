from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Sheet, SheetGroup, Item, Skill, Spell
from . import forms

from django.core.management import call_command

import json

# Create your views here.
def sheetList(request):
    sheets = Sheet.objects.all().order_by('name')
    groups = SheetGroup.objects.all()
    return render(request, 'sheets/sheetList.html', { 'sheets': sheets, 'groups': groups })

def sheetDetail(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    equipment = Item.objects.filter(sht=sheet)
    spells = Spell.objects.filter(sht=sheet)

    return render(
        request, 'sheets/sheetDetail.html', {
            'sheet': sheet,
            'equipment': equipment,
            'slug': slug,
            'request': request,
            'spells': spells,
        })

def createSheet(request):
    form = forms.CreateSheet()
    # for group in SheetGroup.objects.all().order_by('name'):
    #     form.sheetGroup.add(group)

    if request.method == 'POST':
        form = forms.CreateSheet(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('sheets:list')
    else:
        form = forms.CreateSheet()
    return render(request, 'sheets/createSheet.html', { 'form': form })

def editSheet(request, slug):
    call_command('makemigrations')
    call_command('migrate')

    sheet = Sheet.objects.get(slug=slug)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.CreateSheet(request.POST, instance=sheet)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.CreateSheet(instance=sheet)

        return render(request, 'sheets/editSheet.html', { 'form': form, 'slug': slug, 'sheet': sheet })
    else:
        return redirect('sheets:list')

def createGroup(request):
    form = forms.CreateGroup()

    if request.method == 'POST':
        form = forms.CreateGroup(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('sheets:list')
    else:
        form = forms.CreateGroup()
    return render(request, 'sheets/createGroup.html', { 'form': form })

def addItem(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    form = forms.AddItem()

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddItem(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = Sheet.objects.get(slug=slug)

                if Item.objects.filter(sht=instance.sht, name=instance.name).exists():
                    return redirect('sheets:detail', slug=slug)

                instance.save()

                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.AddItem()
            form.sht = Sheet.objects.get(slug=slug)
        return render(request, 'sheets/addItem.html', { 'form': form, 'slug': slug })
    else:
        return redirect('sheets:list')

def editItem(request, name, slug):
    sheet = Sheet.objects.get(slug=slug)
    item = Item.objects.get(name=name, sht=sheet)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddItem(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                item.delete()
                instance.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.AddItem(instance=item)
            return render(request, 'sheets/editItem.html', { 'form': form, 'item': item, 'slug': slug })
    else:
        return redirect('sheets:list')

def removeItem(request, name, slug):
    sheet = Sheet.objects.get(slug=slug)
    item = Item.objects.get(name=name, sht=sheet)

    item.delete()
    return redirect('sheets:detail', slug=slug)

def addSkill(request, slug):
    sheet = Sheet.objects.get(slug=slug)

    if request.user == sheet.author:
        if request.method == 'POST':
            form  = forms.AddSkill(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                instance.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.AddSkill()
            return render(request, 'sheets/addSkill.html', { 'form': form, 'slug': slug })
    else:
        return redirect('sheets:list')

def removeSkill(request, name, slug):
    sheet = Sheet.objects.get(slug=slug)
    skill = Skill.objects.get(name=name, sht=sheet)

    skill.delete()
    return redirect('sheets:detail', slug=slug)

def addSpell(request, slug):
    sheet = Sheet.objects.get(slug=slug)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddSpell(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                instance.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.AddSpell()
            return render(request, 'sheets/addSpell.html', { 'form': form, 'slug': slug })
    else:
        return redirect('sheets:list')

def editSpell(request, name, slug):
    sheet = Sheet.objects.get(slug=slug)
    spell = Spell.objects.get(name=name, sht=sheet)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddSpell(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                spell.delete()
                instance.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.AddSpell(instance=spell)
            return render(request, 'sheets/editSpell.html', { 'form': form, 'spell': spell, 'slug': slug })
    else:
        return redirect('sheets:list')

def removeSpell(request, name, slug):
    sheet = Sheet.objects.get(slug=slug)
    spell = Spell.objects.get(name=name, sht=sheet)

    spell.delete()
    return redirect('sheets:detail', slug=slug)

@csrf_exempt
def ajaxEdit(request, slug):
    value = request.POST.get('value')
    newValue = request.POST.get('newValue')
    
    print(value, newValue)
    sheet = Sheet.objects.get(slug=slug)

    if not newValue.lower().replace(' ', '').isalpha():
        exec('sheet.' + value + " = " + newValue)
    else:
        exec('sheet.' + value + " = '" + newValue + "'")
    sheet.save()


    response = {}
    response['hello'] = 'hello'
    return JsonResponse(response)

def ajaxSheetDetail(request, slug, value):
    sheet = Sheet.objects.filter(slug=slug)
    
    response = {}
    response['sheet'] = json.loads(exec('sheet.' + value))
    return JsonResponse(response)