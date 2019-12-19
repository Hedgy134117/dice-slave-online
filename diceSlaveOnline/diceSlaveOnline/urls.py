from django.contrib import admin
from django.urls import path, include
# from django.conf.urs import url
from . import views

urlpatterns = [
    path('', views.homepage),
    # url('', include('pwa.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sheets/', include('sheets.urls')),
    path('dice/', include('onlineDice.urls')),
    path('accounts/', include('accounts.urls')),
]
