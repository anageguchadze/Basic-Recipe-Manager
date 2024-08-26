from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':recipes})

def recipe_detail(request, name):
    recipe = Recipe.objects.get(name=name)
    return render(request, 'recipe_detail.html', {'recipe':recipe})

def add_recipe(request):
    if request.method == 'POST':
        new_recipe = Recipe(
            name = request.POST.get('name'),
            ingredients = request.POST.get('ingredients'),
            instructions = request.POST.get('instructions'),
        )
        new_recipe.save()
        return redirect('index')
    return render(request, 'add_recipe.html')

def edit_recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.save()
        return redirect('index')
    return render(request, 'edit_recipe.html', {'recipe': recipe})

def delete_recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return render(request, 'delete_recipe.html', {'recipe':recipe})