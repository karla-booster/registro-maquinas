from django.shortcuts import render
from F_registros.models import Registros

# Create your views here.

def nuevoreg(request):
    
    if request.method=='POST':
        if request.POST.get('estado'):
            saverecord=Registros()

            saverecord.estado=request.POST.get('estado')
            return render(request, 'cambio_est.html')
    else:
        return render(request, 'cambio_est.html')
    