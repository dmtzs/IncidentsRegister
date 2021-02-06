from django.contrib import admin
from .models import PageModel

# Register your models here.
admin.site.register(PageModel)
tit= "Page administration"
admin.site.site_header= tit
admin.site.site_title= tit
admin.site.index_title= "Management panel"