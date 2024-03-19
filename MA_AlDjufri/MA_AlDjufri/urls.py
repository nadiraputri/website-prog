
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pendaftaran/', views.pendaftaran),
    path('', views.index),
    path('data/', views.data),
]
   

