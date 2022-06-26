from django.contrib import admin
from .models import Pdf


class pdfAdmin(admin.ModelAdmin):
    list_display = ['დასახელება' , 'pdf']
    ordering = ['დასახელება']


admin.site.site_header = "NOC"
admin.site.register(Pdf,pdfAdmin)
admin.site.site_title = "Noc Admin Portal"
admin.site.index_title = "Welcome to Noc"
