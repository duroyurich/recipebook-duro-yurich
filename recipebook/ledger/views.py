from django.shortcuts import render
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipe_list.html', ctx)


def recipe(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'recipe.html', ctx)
