from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context

from datetime import datetime
from django.shortcuts import render

def bienvenida(request):
    return HttpResponse('<h1>Bienvenido/a a mi primer MVT</h1>')

def index(request):
    return render(request,'template1.html',context = {})
