from D_dept.models import Dept

def get_dept(request):
    
    dept = Dept.objects.values_list('id','name')
    
    return{
        'dept' : dept,
    }
