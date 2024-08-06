from django.contrib import admin
from app.models import Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_id','name', 'description','ingredients','instructions','photo']
admin.site.register(Recipe, RecipeAdmin)