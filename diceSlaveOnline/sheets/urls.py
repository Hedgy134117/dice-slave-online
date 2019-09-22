from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.sheetList, name='list'),
    path('create/', views.createSheet, name='create'),
    path('big', views.bigSheetList, name='bigList'),
    path('edit/<slug:slug>/', views.editSheet, name='edit'),
    path('<slug:slug>/', views.sheetDetail, name="detail")
]