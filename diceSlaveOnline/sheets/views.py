from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Sheet, SheetGroup
from . import forms

from django.core.management import call_command

# Create your views here.
def sheetList(request):
    sheets = Sheet.objects.all().order_by('name')
    groups = SheetGroup.objects.all().order_by('name')
    return render(request, 'sheets/sheetList.html', { 'sheets': sheets, 'groups': groups })

def sheetDetail(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    return render(request, 'sheets/sheetDetail.html', { 'sheet': sheet, 'slug': slug, 'request': request })

def createSheet(request):
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

    for group in SheetGroup.objects.all().order_by('name'):
        sheet.sheetGroup.add(group)

    sheet.save()
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

