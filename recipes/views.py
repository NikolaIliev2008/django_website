from django.shortcuts import render

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
    context = {'recipes': recipes}
    return render(request, "recipes/home.html", context)

def about(request):
        return render(request, "recipes/about.html")
