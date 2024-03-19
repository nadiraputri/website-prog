from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def pendaftaran(request):
    return render(request,'pendaftaran.html')

def data(request):
    return render(request, 'data.html')