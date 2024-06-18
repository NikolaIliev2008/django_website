from django.shortcuts import render
from . import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Recipe
from rest_framework import viewsets
from django.urls import reverse_lazy
from .serializers import RecipeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

      

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

@api_view(['GET','POST'])
def recipe_list(request):

      if request.method == 'GET':
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
      
      if request.method == 'POST':
          serializer = RecipeSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','GET','DELETE','PATCH'])
def recipe_detail(request,id,self):

      try:
            recipe = Recipe.objects.get(pk=id)
      except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
      
      if request.method == 'GET':
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
      
      elif request.method == 'PUT':
           serializer = RecipeSerializer(recipe, data=request.data)
           if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      elif request.method == 'DELETE':
           recipe.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
      
      elif request.method == 'PATCH':
            recipe = self.get_object()
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)