from tokenize import group
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Pdf

class pdfAdmin(admin.ModelAdmin):
    list_display = ['დასახელება' , 'pdf']
    ordering = ['დასახელება']


admin.site.site_header = "NOC"
admin.site.register(Pdf,pdfAdmin)


 