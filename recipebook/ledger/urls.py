from django.urls import path
from .views import recipes_list, recipe

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/<int:id>', recipe, name='recipe-detail'),
]

app_name = 'ledger'
