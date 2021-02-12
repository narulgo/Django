from django.contrib import admin
from .models import Comment, Element, Category, Type
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ElementResource(resources.ModelResource):

    class Meta:
        model = Element
        fields = ('id','title','url_clean','category','type')


class ElementAdmin(ImportExportModelAdmin):
    resource_class=ElementResource
    list_display = ('id','title')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')


admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Comment)
