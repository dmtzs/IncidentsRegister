from django.contrib import admin
from .models import RegIncident

# Register your models here.
#class CategoryAdmin(admin.ModelAdmin):
    #readonly_fields= ("created at")

class IncidentAdmin(admin.ModelAdmin):
    readonly_fields= ("created_at", "updated_at")

#admin.site.register(Category, CategoryAdmin)
admin.site.refister(RegIncident, IncidentAdmin)