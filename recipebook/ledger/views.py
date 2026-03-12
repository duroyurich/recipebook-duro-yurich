from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, ImageForm


def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'recipe.html', ctx)


@login_required
def recipe_add(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('ledger:recipe-detail', id=recipe.id)
    ctx = {"recipe": Recipe.objects.all(), "form": form}
    return render(request, 'recipe_add.html', ctx)


@login_required
def recipe_add_image(request, id):
    recipe = Recipe.objects.get(id=id)
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe-detail', id=recipe.id)
    ctx = {"recipe": recipe, "form": form}
    return render(request, 'recipe_add_image.html', ctx)
