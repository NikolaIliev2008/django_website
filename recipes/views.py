from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer
from django.urls import reverse_lazy
from django.http import HttpResponse

      

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
        return super().form_valid(form)   


class RecipeUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
      model = models.Recipe
      fields = ['title', 'description']  

       
      def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
  

      def form_valid(self, form):  
        form.instance.author = self.request.user   
        return super().form_valid(form)
      
     
class RecipeDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
      model = models.Recipe
      success_url = reverse_lazy('home')
       
      def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


def about(request):
        return render(request, "recipes/about.html")

