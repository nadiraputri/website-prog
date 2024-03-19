
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pendaftaran/', views.pendaftaran),
    path('', views.index),
    path('data/', views.data),
    path('datasiswa/', views.datasiswa),
    path('dataortu/', views.dataortu),
    path('pekerjaan/', views.pekerjaan),
    path('asalsekolah/', views.asalsekolah),
]
   

