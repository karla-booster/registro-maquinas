from C_maquinas.models import Area, Maquina

def get_areas(request):
    
    areas = Area.objects.values_list('id','name')
    
    return{
        'areas' : areas,
    }

def get_maquinas(request):
    
    maquinas = Maquina.objects.values_list('id','title','area')
    
    return{
        'maquinas' : maquinas,
    }
