from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from C_maquinas.models import Area, Maquina
from E_estados.models import Estados
from F_registros.models import Registros
from D_dept.models import Dept
from H_material.models import pp, RegProd 

# Create your views here.

@login_required(login_url='login')
def list(request):

    #Sacar maquinas
    maquinas = Maquina.objects.all()

    #Paginar las maquinas
    paginator = Paginator(maquinas, 15)

    #Recoger numero pagina
    page= request.GET.get('page')
    page_maquinas=paginator.get_page(page)

    return render(request,'maquinas/list.html',{
        'title':'Máquinas',
        'maquinas': page_maquinas
    })


@login_required(login_url='login')
def area(request, area_id):

    area = get_object_or_404(Area, id=area_id)
    maquinas=Maquina.objects.filter(area=area).order_by('-title')
    
    return render(request,'areas/area.html',{
        'area': area,
        'maquinas':maquinas,
    })


@login_required(login_url='login')
def maquina(request, maquina_id):
    maquina = get_object_or_404(Maquina, id=maquina_id)

    registroact= Registros.objects.filter(active=True, maquina=maquina.title).values()
    registrohist= Registros.objects.filter(active=False, maquina=maquina.title ).order_by('-cambio').values()[:25]

    dep = request.user.last_name
    dept= Dept.objects.get(name=dep)
    op_estados= Estados.objects.filter(departamento=dept).values('id','estado')
    area_id= Maquina.objects.filter(id=maquina_id).values_list('area')
    area= Area.objects.filter(id__in=area_id).values_list('name')
    today=datetime.now()
    #mail = User.objects.filter(username=request.user.username).values(email)
    email=request.user.email

    if email == 'nuno@gmail.com':
        nivel=3
    elif email == 'ndos@gmail.com':
        nivel=2
    else:
        nivel=3

    if request.method =='POST':
        
        estado=request.POST.get('estado')
    
        if estado != '':
            check=Registros.objects.filter(maquina=maquina, active=True).values_list()

            if not check:
                Registros.objects.create(
                    maquina= maquina,
                    area= area,
                    estado= Estados.objects.filter(id=estado).values_list('estado'),
                    usuario= request.user.username,
                    departamento = dept,
                    active= True
                )
            else:
                act= Registros.objects.filter(maquina=maquina, active=True).get()
                act.active= False
                act.save()

                Registros.objects.create(
                    maquina= maquina,
                    area= area,
                    estado= Estados.objects.filter(id=estado).values_list('estado'),
                    usuario= request.user.username,
                    departamento = dept,
                    active= True
                )

    return render(request, 'maquinas/detail.html', {
        'maquina':maquina,
        'op_estados':op_estados,
        'dept':dep,
        'registroact':registroact,
        'registrohist':registrohist,
        'today':today,
        'nivel':nivel,
    })
