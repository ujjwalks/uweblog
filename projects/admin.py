from django.contrib import admin

from .models import RequestProject
from .models import SelfProject
from .models import WorkProject

# Register your models here.

admin.site.register(RequestProject)
admin.site.register(SelfProject)
admin.site.register(WorkProject)
