# products/admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image_preview', 'created_at', 'updated_at')  # 加入 created_at 和 updated_at

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" />'
        return '無圖片'
    image_preview.allow_tags = True
    image_preview.short_description = '圖片預覽'

admin.site.register(Product, ProductAdmin)
