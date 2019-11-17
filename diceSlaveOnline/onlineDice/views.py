from django.shortcuts import render
from django.apps import apps

Sheet = apps.get_model('sheets', 'Sheet')

# Create your views here.
def base(request):
    sheet = Sheet.objects.filter(author=request.user)

    if sheet.count() > 1:
        return render(request, 'onlineDice/base.html', { 'sheet': False })
    else:
        sheet = sheet[0]

    return render(request, 'onlineDice/base.html', { 'sheet': sheet } )