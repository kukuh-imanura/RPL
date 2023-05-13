from django.shortcuts import render

# Create your views here.

from . models import DaftarSiswa

def index(request) :

    

    return render(request, 'daftar/index.html')