from django.contrib import admin
from .models import Verif

# Register your models here.
class VerAdmin(admin.ModelAdmin):
    list_display=('verf',)
    search_fields=('verf',)


# Register your models here.
admin.site.register(Verif, VerAdmin)