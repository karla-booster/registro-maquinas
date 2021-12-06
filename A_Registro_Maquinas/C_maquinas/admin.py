from django.contrib import admin
from .models import Area, Maquina

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)

class MaquinaAdmin(admin.ModelAdmin):
    search_fields=('title', 'area')
    list_display=('title', 'public')


# Register your models here.
admin.site.register(Area, AreaAdmin)
admin.site.register(Maquina, MaquinaAdmin)