from F_registros.models import Registros
from D_dept.models import Dept
from django.contrib.auth.models import User

def get_registros(request):
    
    registros_in_use = Registros.objects.filter(active=True).values_list()
    registros = Registros.objects.filter(id__in=registros_in_use).values_list()
    
    return{
        'registros' : registros,
        'reg_act' : registros_in_use
    }

def get_userdept(request):
    dept= request.user.last_name
    userdept = Registros.objects.filter(name__in=dept).values_list('id','name')
    
    return{
        'userdept' : userdept,
    }