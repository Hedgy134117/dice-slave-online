from django.urls import path
from . import views

app_name = "dice"

urlpatterns = [
    path('', views.base, name='base'),
]