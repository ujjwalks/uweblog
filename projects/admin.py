from django.contrib import admin

from .models import RequestProject
from .models import SelfProject
from .models import WorkProject
from .models import Images

# Register your models here.

admin.site.register(RequestProject)
admin.site.register(SelfProject)

class ImageInline(admin.TabularInline):
    model = Images
    extra = 3

class WorkProjectAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, ]
    
admin.site.register(WorkProject, WorkProjectAdmin)