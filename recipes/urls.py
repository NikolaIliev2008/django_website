from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('',views.RecipeListView.as_view(), name="home"),
    path('recipe/create',views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>',views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/update',views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete',views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('recipes/',views.recipe_list),
    path('recipes/<int:id>',views.recipe_detail),

    path('about/',views.about, name="about-page"),
]