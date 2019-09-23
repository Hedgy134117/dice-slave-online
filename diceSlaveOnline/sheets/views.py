from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Sheet
from . import forms

# Create your views here.
def sheetList(request):
    sheets = Sheet.objects.all().order_by('name')
    return render(request, 'sheets/sheetList.html', { 'sheets': sheets })

def sheetDetail(request, slug):
    sheet = Sheet.objects.get(slug=slug)
    return render(request, 'sheets/sheetDetail.html', { 'sheet': sheet, 'slug': slug })

def createSheet(request):
    if request.method == 'POST':
        form = forms.CreateSheet(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sheets:list')
    else:
        form = forms.CreateSheet()
    return render(request, 'sheets/createSheet.html', { 'form': form })

def editSheet(request, slug):
    sheet = Sheet.objects.get(slug=slug)

    if request.method == 'POST':
        form = forms.CreateSheet(request.POST, instance=sheet)

        if form.is_valid():
            form.save()
            return redirect('sheets:list')
    else:
        form = forms.CreateSheet(instance=sheet)
    return render(request, 'sheets/editSheet.html', { 'form': form, 'slug': slug })