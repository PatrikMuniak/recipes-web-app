from django.db import models

# Create your models here.
class RecipesModel(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=70)
    ingredients = models.CharField(max_length=255)
    recipe_description = models.CharField(max_length=500)
