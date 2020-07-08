from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.sheetList, name='list'),
    path('createGroup/', views.createGroup, name='createGroup'),
    
    # ---------- SHEET ---------- # 
    path('sheet/<id>/', views.sheetDetail, name="detail"),
    path('sheetNew/<id>/', views.sheetDetail_new, name='newDetail'),
    path('create/', views.createSheet, name='create'),
    path('edit/<id>/', views.editSheet, name='edit'),
    path('<id>/get/', views.ajaxSheetDetail, name='ajaxDetail'),
    path('<id>/post/', views.ajaxEdit, name="ajaxEdit"),

    # ---------- ITEMS ---------- # 
    path('addItem/<id>/', views.addItem, name='addItem'),
    path('editItem/<itemID>/<sheetID>/', views.editItem, name='editItem'),
    path('removeItem/<itemID>/<sheetID>/', views.removeItem, name='removeItem'),
    path('items/<id>/get/', views.ajaxItem, name='ajaxItem'),
    path('items/<id>/add/', views.ajaxAddItem, name='ajaxAddItem'),
    path('items/<id>/post/', views.ajaxItemEdit, name='ajaxItemEdit'),
    path('items/<id>/remove/', views.ajaxItemRemove, name='ajaxItemRemove'),

    # ---------- (UNUSED) SKILLS ---------- # 
    path('addSkill/<slug:slug>/', views.addSkill, name='addSkill'),
    path('removeSkill/<str:name>/<slug:slug>/', views.removeSkill, name='removeSkill'),

    # ---------- SPELLS ---------- # 
    path('addSpell/<id>/', views.addSpell, name='addSpell'),
    path('editSpell/<spellID>/<sheetID>/', views.editSpell, name='editSpell'),
    path('removeSpell/<spellID>/<sheetID>/', views.removeSpell, name='removeSpell'),

    
]