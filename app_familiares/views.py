from django.shortcuts import render
from app_familiares.models import App_Familiares

# Create your views here.
def familiares_vis(request):
    fam_1 = App_Familiares.objects.create(
        nombre = "Vito Corleone",
        fecha_nacimiento = '1891-12-07',
        observaciones = 'Padre de Michael Corleone')
    fam_2 = App_Familiares.objects.create(
        nombre = "Michael Corleone",
        fecha_nacimiento = '1922-10-15',
        observaciones = 'Lider en Nueva York')
    fam_3 = App_Familiares.objects.create(
        nombre = "Fredo Corleone",
        fecha_nacimiento = '1919-05-13',
        observaciones = 'Hijo de Vito y hermano de Michael. Traidor')
    context = {'fam_1':fam_1,'fam_2':fam_2,'fam_3':fam_3}
    return render(request,'familiares.html',context=context)
