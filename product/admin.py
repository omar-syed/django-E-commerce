from django.contrib import admin
from.models import Product,ProductImage,Category,Product_Alternative,Product_Accessories
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['PRDName', 'PRDSLug', 'PRDPrice','PRDAvailable', 'PRDCreated', 'PRDUpdated']
    list_filter = ['PRDAvailable', 'PRDCreated', 'PRDUpdated', 'PRDPrice']
    list_editable = ['PRDPrice', 'PRDAvailable']
    prepopulated_fields = {'PRDSLug': ('PRDName',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['CATName', 'CATSlug']
    prepopulated_fields = {'CATSlug': ('CATName',)}

#admin.site.register(Product)
admin.site.register(ProductImage)
#admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)



