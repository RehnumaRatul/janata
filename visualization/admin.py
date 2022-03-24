from django.contrib import admin
from .models import VisualData
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VisualResource(resources.ModelResource):
   class Meta:
      model = VisualData
class VisualAdmin(ImportExportModelAdmin):
   resource_class = VisualResource

admin.site.register(VisualData,VisualAdmin)