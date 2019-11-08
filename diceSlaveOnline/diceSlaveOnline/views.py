from django.shortcuts import render, redirect
from sheets.models import Sheet

def homepage(request):
    if request.user.is_authenticated != True:
        return render(request, 'homepage.html', {})
    else:
        return redirect('profile', request.user)

def profile(request, username):
    sheets = Sheet.objects.filter(author=request.user)

    return render(request, 'profile.html', {'sheets': sheets})