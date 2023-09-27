from django.contrib import admin
from .models import Food, Cart

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    ordering = ('name', 'type')
    search_fields = ('name', 'type')
    list_filter = ('type', 'price')
    
    pass

admin.site.register(Food, FoodAdmin)
admin.site.register(Cart)