from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.sheetList, name='list'),
    path('create/', views.createSheet, name='create'),
    path('edit/<slug:slug>/', views.editSheet, name='edit'),
    path('addItem/<slug:slug>/', views.addItem, name='addItem'),
    path('<slug:slug>/', views.sheetDetail, name="detail")
]