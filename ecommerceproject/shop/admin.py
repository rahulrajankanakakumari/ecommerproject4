from django.contrib import admin

# Register your models here.
from.models import category,Product

class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page=20
admin.site.register(Product,ProductAdmin)
