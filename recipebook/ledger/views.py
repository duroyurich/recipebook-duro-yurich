from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'recipe.html', ctx)
