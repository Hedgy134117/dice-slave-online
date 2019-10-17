from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Sheet, SheetGroup, Item
from . import forms

from django.core.management import call_command

# Create your views here.
def sheetList(request):
    sheets = Sheet.objects.all().order_by('name')
    groups = SheetGroup.objects.all()
    return render(request, 'sheets/sheetList.html', { 'sheets': sheets, 'groups': groups })

def sheetDetail(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    itemList = Item.objects.all()
    equipment = []
    for item in itemList:
        if item.sht == sheet:
            equipment.append(item)
    return render(request, 'sheets/sheetDetail.html', { 'sheet': sheet, 'equipment': equipment, 'slug': slug, 'request': request })

def createSheet(request):
    form = forms.CreateSheet()
    # for group in SheetGroup.objects.all().order_by('name'):
    #     form.sheetGroup.add(group)

    if request.method == 'POST':
        form = forms.CreateSheet(request.POST)
        form.author = request.user

        if form.is_valid():
            form.save()
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
                form.save()
                return redirect('sheets:detail', slug=slug)
        else:
            form = forms.CreateSheet(instance=sheet)

        return render(request, 'sheets/editSheet.html', { 'form': form, 'slug': slug })
    else:
        return redirect('sheets:list')

def addItem(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    form = forms.AddItem()

    if request.user == sheet.author:
        if request.method == 'POST':
            form = forms.AddItem(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.sht = Sheet.objects.get(slug=slug)
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

