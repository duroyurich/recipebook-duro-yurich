from django.contrib import admin
from .models import Recipe, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


admin.site.register(Recipe, RecipeAdmin)
