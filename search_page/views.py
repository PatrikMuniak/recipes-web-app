from django.shortcuts import render
from recipe_page.models import RecipesModel

# Create your views here.
def SearchViews(request):

    query = request.GET.get("q")
    results = RecipesModel.objects.all().filter(ingredients=query)
    print([p.recipe_name for p in results])
    
    context = {
        'results': results,
    }
    return render(request, 'search_page.html',context)
