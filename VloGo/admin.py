from django.contrib import admin
from .models import Food, Cart
# ▲ spacja
class FoodAdmin(admin.ModelAdmin)
    list_display = ('id', display_name, 'name')
    
    pass

admin.site.register(Food, FoodAdmin)
admin.site.register(Cart)