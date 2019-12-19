from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required

Sheet = apps.get_model('sheets', 'Sheet')

# Create your views here.
@login_required
def base(request):
    sheet = Sheet.objects.filter(author=request.user)

    if sheet.count() > 1:
        return render(request, 'onlineDice/base.html', { 'sheet': False })
    else:
        try:
            sheet = sheet[0]
        except:
            return render(request, 'onlineDice/base.html', { 'sheet': False })

    return render(request, 'onlineDice/base.html', { 'sheet': sheet } )