from django.contrib import admin
from .models import Estados

# Register your models here.
class EstAdmin(admin.ModelAdmin):
    list_display=('estado',)
    search_fields=('estado',)


# Register your models here.
admin.site.register(Estados, EstAdmin)