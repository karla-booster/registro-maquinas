from E_estados.models import Estados

def get_estados(request):
    
    estados = Estados.objects.values_list('estado','departamento','colorfondo','colorletra')

    
    return{
        'estados' : estados,
    }
