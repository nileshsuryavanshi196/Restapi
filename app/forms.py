from .models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"