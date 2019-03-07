from django.contrib import admin

from .models import PortAllocation

class PortAllocationAdmin(admin.ModelAdmin):
    list_display = ('port_number','student')
    search_fields = ['port_number']

admin.site.register(PortAllocation, PortAllocationAdmin)