from django.shortcuts import render
from .models import RecipesModel


# Create your views here.
def RecipeViews(request):
    query = request.GET.get("recipe_name")
    print(query+' from recipe_page')
    recipe = RecipesModel.objects.get(recipe_name=query)
    print(recipe.recipe_description)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe_page.html', context)
