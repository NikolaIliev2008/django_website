from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

recipes = [
    {
      'author': 'Tom',
      'title': 'meatball sub',
      'directions': 'combine everything',
      'date_posted': 'June 2024'
    },
    {
      'author': 'Niki',
      'title': 'turkey sub',
      'directions': 'combine everything',
      'date_posted': 'March 2024'
    },
    {
      'author': 'Tony',
      'title': 'Chicken sub',
      'directions': 'combine everything',
      'date_posted': 'July 2024'
    }
]


def home(request):
    recipes = models.Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
      model = models.Recipe
      template_name = 'recipes/home.html'
      context_object_name = 'recipes'

class RecipeDetailView(DetailView):
      model = models.Recipe

class RecipeCreateView(CreateView, LoginRequiredMixin):
      model = models.Recipe
      fields = ['title', 'description']    

def form_valid(self, form):  
   form.instance.author = self.request.user   
   return super(RecipeCreateView, self).form_valid(form)

def about(request):
        return render(request, "recipes/about.html")
