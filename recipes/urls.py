from django.urls import path
from . import views

urlpatterns = [
    path('',views.RecipeListView.as_view(), name="home"),
    path('recipe/create',views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>',views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('about/',views.about, name="about-page"),
]