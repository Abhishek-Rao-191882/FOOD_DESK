from django.contrib import admin

# Register your models here.
from .models import categories, products
# admin.site.register(client)
admin.site.register(categories)
admin.site.register(products)