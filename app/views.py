from django.shortcuts import render,redirect
from .models import Recipe
from .forms import RecipeForm
from .serializers import Recipeserializer
from rest_framework import generics
from django.db.models import Q


# Create your views here.

def recipeform(req):
    if req.method == 'POST':
        form = RecipeForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            print("success submit")
            return redirect('/')
        else:
            print("invalid form",form.errors)
    else:
        form=RecipeForm()
    context = {'form':form}
    return render(req,'recipe_form.html', context)

def dashboard(req):
    allrecipe = Recipe.objects.all()
    context = {"allrecipe": allrecipe}
    return render(req,'dashboard.html',context)


def updaterecipe(req, recipe_id):
    reciperecord = Recipe.objects.get(recipe_id=recipe_id)
    if req.method == "POST":
        form = RecipeForm(req.POST, req.FILES, instance=reciperecord)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RecipeForm(instance=reciperecord)

    context = {"form": form, "reciperecord": reciperecord}
    return render(req, "updaterecipe.html", context)

def removerecipe(req, recipe_id):
    reciperecord = Recipe.objects.get(recipe_id=recipe_id)
    reciperecord.delete()
    return redirect("/")


def searchrecipe(req):
    query = req.GET.get("q")
    errmsg = ""
    
    if query:
        allrecipe = Recipe.objects.filter(
                Q(name__icontains=query) | Q(recipe_id__icontains=query)
            )
    else:
        allrecipe = Recipe.objects.all()
    context = {"allrecipe": allrecipe, "query": query, "errmsg": errmsg}
    return render(req, 'dashboard.html', context)


class Viewsapi(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer

class Createapi(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer

class Updateapi(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    lookup_field='recipe_id'

class Deleteapi(generics.RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    lookup_field='recipe_id'

