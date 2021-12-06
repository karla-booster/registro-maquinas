from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, timezone
from django.db.models import Sum

from django.contrib.auth.models import User
from C_maquinas.models import Area, Maquina
from E_estados.models import Estados
from F_registros.models import Registros
from D_dept.models import Dept
from H_material.models import pp, RegProd 
from G_Verif.models import Verif
from I_calidad.models import Aprobar_piezas

# Create your views here.

@login_required(login_url='login')
def aprobar(request):

    maqcw = Maquina.objects.filter(area=1).order_by('-title').values('title')
    maqshaft = Maquina.objects.filter(area=2).order_by('-title').values('title')
    maqdvg = Maquina.objects.filter(area=3).order_by('-title').values('title')

    if request.method =='POST':
        
        reset=request.POST.get('reset')


        if reset == reset:
            for maquina in maqcw:
                a= Aprobar_piezas.objects.filter(maquina=maquina).values_list()

                if not a:
                    Aprobar_piezas.objects.create(
                    maquina= maquina,
                    area= "C. W.",
                    recibida= False,
                    aprobada= False,
                    rechazada= False,
                )
                else:
                    a.recibida= False
                    a.aprobada= False
                    a.rechazada= False
                    a.save()
            
            for maquina in maqdvg:
                a= Aprobar_piezas.objects.filter(maquina=maquina).values_list()

                if not a:
                    Aprobar_piezas.objects.create(
                    maquina= maquina,
                    area= "DVG",
                    recibida= False,
                    aprobada= False,
                    rechazada= False,
                )
                else:
                    a.recibida= False
                    a.aprobada= False
                    a.rechazada= False
                    a.save()
            
            for maquina in maqshaft:
                a= Aprobar_piezas.objects.filter(maquina=maquina).values_list()

                if not a:
                    Aprobar_piezas.objects.create(
                    maquina= maquina,
                    area= "SHAFT",
                    recibida= False,
                    aprobada= False,
                    rechazada= False,
                )
                else:
                    a.recibida= False
                    a.aprobada= False
                    a.rechazada= False
                    a.save()

    return render(request, 'piezas/aprobar_piezas.html', {
        'maqcw':maqcw,
        'maqshaft':maqshaft,
        'maqdvg':maqdvg,
    })
