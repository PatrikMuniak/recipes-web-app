from django.shortcuts import render
from .forms import FoodsForm


# Create your views here.
def FoodsView(request):
    form = FoodsForm(request.GET or None)
    if form.is_valid():
        food = form.cleaned_data['food']
        print(food)

    context = {
        'form': form,
        }
    return render(request, 'main_page.html', context)
