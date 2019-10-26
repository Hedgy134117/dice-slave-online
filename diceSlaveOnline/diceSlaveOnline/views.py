from django.http import HttpResponse
from django.shortcuts import render, redirect

from sheets.models import Sheet, SheetGroup

def homepage(request):
    if request.user.is_authenticated != True:
        return redirect('sheets:list')
    else:
        return redirect('profile', request.user)

def profile(request, username):
    sheets = Sheet.objects.filter(author=request.user)

    return render(request, 'profile.html', {'sheets': sheets})