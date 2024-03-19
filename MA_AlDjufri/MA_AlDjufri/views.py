from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def pendaftaran(request):
    return render(request,'pendaftaran.html')

def data(request):
    return render(request, 'data.html')

def datasiswa(request):
    return render(request, 'datasiswa.html')

def dataortu(request):
    return render(request, 'dataortu.html')

def pekerjaan(request):
    return render(request, 'pekerjaan.html')

def asalsekolah(request):
    return render(request, 'asalsekolah.html')