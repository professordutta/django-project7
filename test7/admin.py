from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class informationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Employee, informationAdmin)
