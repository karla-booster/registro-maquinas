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


    # Registros
    registroact= Registros.objects.filter(active=True, maquina=maquina.title).values()
    if registroact:
        ract=registroact[0]
        r=ract.get('id_estado')
    else:
        r=0
    registrohist= Registros.objects.filter(active=False, maquina=maquina.title ).order_by('-cambio').values()[:25]
    creado=Registros.objects.filter(active=True, maquina=maquina.title)
    if creado:
        creado=Registros.objects.filter(active=True, maquina=maquina.title)[0]
        today=datetime.now(timezone.utc) - creado.created_at
    else:
        today=0

    # Ver nivel de usuario
    email=request.user.email

    if email == 'nuno@gmail.com':
        nivel=1
    elif email == 'ndos@gmail.com':
        nivel=2
    else:
        nivel=3

    # Secuencia de estados
    if r in (0,1,2,14,17,19,20,21):
        op=[1,2,3,4,5,6,11,13,16,17,22,23]
    elif r in (3,12):
        op=[10]
    elif r == 4:
        op=[14]
    elif r == 5:
        op=[1,3,6,9,20]
    elif r == 6:
        op=[7]
    elif r == 7:
        op=[1,3,4,17,20]
    elif r == 8:
        op=[1,3,9]
    elif r == 9:
        op=[18]
    elif r == 10:
        op=[8,12,13,23]
    elif r == 11:
        op=[8,9,12,13,23]
    elif r == 13:
        op=[8,9]
    elif r == 15:
        op=[19]
    elif r == 16:
        op=[3,4,17,20,23]
    elif r == 18:
        op=[8,15,19]
    elif r == 22:
        op=[8]
    elif r == 23:
        op=[22]

    dep = request.user.last_name
    dept= Dept.objects.get(name=dep)
    op_estados= Estados.objects.filter(departamento=dept, nivel__gt=nivel, id__in=op).values('id','estado')
    area_id= Maquina.objects.filter(id=maquina_id).values_list('area')
    area= Area.objects.filter(id__in=area_id).values_list('name')
    
    # Ordenes
    ordenact= pp.objects.filter(maquina=maquina.title).values()[1]
    orden=pp.objects.filter(maquina=maquina.title).values_list('orden')
    sum = RegProd.objects.filter(orden__in=orden, maquina=maquina.title).aggregate(sum=Sum('qtyprod')).get('sum')
    prxorden= pp.objects.filter(maquina=maquina.title).order_by('fecha').values()

    # Recibir cambios
    if request.method =='POST':
        
        estadoss=request.POST.get('estado')
        commentss=request.POST.get('comment')

        if estadoss == -1:
            nada=1
        else:
            if estadoss != '':
                check=Registros.objects.filter(maquina=maquina, active=True).values_list()

                if not check:
                    Registros.objects.create(
                        maquina= maquina,
                        area= area,
                        id_estado=estadoss,
                        estado= Estados.objects.filter(id=estadoss).values_list('estado'),
                        usuario= request.user.username,
                        departamento = dept,
                        active= True,
                        comment=commentss,
                    )
                else:
                    act= Registros.objects.filter(maquina=maquina, active=True).get()
                    act.active= False
                    act.save()

                    Registros.objects.create(
                        maquina= maquina,
                        area= area,
                        id_estado=estadoss,
                        estado= Estados.objects.filter(id=estadoss).values_list('estado'),
                        usuario= request.user.username,
                        departamento = dept,
                        active= True,
                        comment=commentss,
                    )


    return render(request, 'maquinas/detail.html', {
        'maquina':maquina,
        'op_estados':op_estados,
        'dept':dep,
        'registroact':registroact,
        'registrohist':registrohist,
        'today':today,
        'nivel':nivel,
        'ordenact':ordenact,
        'sum':sum,
        'prxorden':prxorden,
    })
