from django.contrib import admin
from .models import Dept

# Register your models here.
class DeptAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)


# Register your models here.
admin.site.register(Dept, DeptAdmin)