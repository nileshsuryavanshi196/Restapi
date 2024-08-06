from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    photo = models.ImageField(upload_to="images")


