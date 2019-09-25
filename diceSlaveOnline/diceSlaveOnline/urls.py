from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('sheets/', include('sheets.urls')),
    path('accounts/', include('accounts.urls')),
]
