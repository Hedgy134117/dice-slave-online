from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.sheetList, name='list'),
    path('create/', views.createSheet, name='create'),
    path('edit/<slug:slug>/', views.editSheet, name='edit'),

    path('addItem/<slug:slug>/', views.addItem, name='addItem'),
    path('editItem/<str:name>/<slug:slug>/', views.editItem, name='editItem'),
    path('removeItem/<str:name>/<slug:slug>/', views.removeItem, name='removeItem'),

    path('addSkill/<slug:slug>/', views.addSkill, name='addSkill'),
    path('removeSkill/<str:name>/<slug:slug>/', views.removeSkill, name='removeSkill'),

    path('addSpell/<slug:slug>/', views.addSpell, name='addSpell'),

    path('<slug:slug>/', views.sheetDetail, name="detail")
]