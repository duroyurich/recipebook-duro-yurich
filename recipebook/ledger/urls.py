from django.urls import path
from .views import recipes_list, recipe, recipe_add, recipe_add_image

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/<int:id>', recipe, name='recipe-detail'),
    path('recipe/add', recipe_add, name="recipe-add"),
    path('recipe/<int:id>/add_image', recipe_add_image, name='recipe-add-image')
]

app_name = 'ledger'
