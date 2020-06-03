from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Sheet, SheetGroup, Item, Skill, Spell
from . import forms

from django.core.management import call_command
from django.urls import reverse

import json


def sheetList(request):
    sheets = Sheet.objects.all().order_by('name')
    groups = SheetGroup.objects.all()
    return render(request, 'sheets/sheetList.html', { 'sheets': sheets, 'groups': groups })

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

# ---------- SHEET ---------- # 
def sheetDetail(request, id):
    sheet = Sheet.objects.get(id=id)
    equipment = Item.objects.filter(sht=sheet)
    spells = Spell.objects.filter(sht=sheet)

    return render(
        request, 'sheets/sheetDetail.html', {
            'sheet': sheet,
            'equipment': equipment,
            'id': id,
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

def editSheet(request, id):
    call_command('makemigrations')
    call_command('migrate')

    sheet = Sheet.objects.get(id=id)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.CreateSheet(request.POST, instance=sheet)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('sheets:detail', id=id)
        else:
            form = forms.CreateSheet(instance=sheet)

        return render(request, 'sheets/editSheet.html', { 'form': form, 'id': id, 'sheet': sheet })
    else:
        return redirect('sheets:list')

@csrf_exempt
def ajaxEdit(request, id):
    value = request.POST.get('value')
    newValue = request.POST.get('newValue')
    
    print(value, newValue)
    sheet = Sheet.objects.get(id=id)

    if not newValue.lower().replace(' ', '').isalpha():
        exec('sheet.' + value + " = " + newValue)
    else:
        exec('sheet.' + value + " = '" + newValue + "'")
    sheet.save()


    response = {}
    response['hello'] = 'hello'
    return JsonResponse(response)

def ajaxSheetDetail(request, id):
    sheet = Sheet.objects.filter(id=id)
    
    response = {}
    response['sheet'] = json.loads(serializers.serialize("json", sheet))
    return JsonResponse(response)

# ---------- ITEMS ---------- # 
def addItem(request, id):
    title = "Add an Item"
    action = "Add"
    url = reverse('sheets:addItem', args=[id])

    sheet = Sheet.objects.get(id=id)
    form = forms.AddItem()

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddItem(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = Sheet.objects.get(id=id)

                if Item.objects.filter(sht=instance.sht, name=instance.name).exists():
                    return redirect('sheets:detail', id=id)

                instance.save()

                return redirect('sheets:detail', id=id)
        else:
            form = forms.AddItem()
            form.sht = Sheet.objects.get(id=id)
        return render(request, 'sheets/sheetForm.html', { 'form': form, 'title': title, 'action': action, 'url': url })
    else:
        return redirect('sheets:list')

def editItem(request, itemID, sheetID):
    title = "Edit an Item"
    action = "Edit"
    url = reverse('sheets:editItem', args=[itemID, sheetID])

    sheet = Sheet.objects.get(id=sheetID)
    item = Item.objects.get(id=itemID)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddItem(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                item.delete()
                instance.save()
                return redirect('sheets:detail', id=sheetID)
        else:
            form = forms.AddItem(instance=item)
            return render(request, 'sheets/sheetForm.html', { 'form': form, 'title': title, 'action': action, 'url': url })
    else:
        return redirect('sheets:list')

def removeItem(request, itemID, sheetID):
    sheet = Sheet.objects.get(id=sheetID)
    item = Item.objects.get(id=itemID)

    item.delete()
    return redirect('sheets:detail', id=sheetID)

# ---------- (UNUSED) SKILLS ---------- # 
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

# ---------- SPELLS ---------- # 
def addSpell(request, id):
    title = "Add a Spell"
    action = "Add"
    url = reverse('sheets:addSpell', args=[id])

    sheet = Sheet.objects.get(id=id)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddSpell(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                instance.save()
                return redirect('sheets:detail', id=id)
        else:
            form = forms.AddSpell()
            return render(request, 'sheets/sheetForm.html', { 'form': form, 'title': title, 'action': action, 'url': url })
    else:
        return redirect('sheets:list')

def editSpell(request, spellID, sheetID):
    title = "Edit a Spell"
    action = "Edit"
    url = reverse('sheets:editSpell', args=[spellID, sheetID])

    sheet = Sheet.objects.get(id=sheetID)
    spell = Spell.objects.get(id=spellID)

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddSpell(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = sheet
                spell.delete()
                instance.save()
                return redirect('sheets:detail', id=sheetID)
        else:
            form = forms.AddSpell(instance=spell)
            return render(request, 'sheets/sheetForm.html', { 'form': form, 'title': title, 'action': action, 'url': url })
    else:
        return redirect('sheets:list')

def removeSpell(request, spellID, sheetID):
    sheet = Sheet.objects.get(id=sheetID)
    spell = Spell.objects.get(id=spellID)

    spell.delete()
    return redirect('sheets:detail', id=sheetID)