from django.db import models

# Create your models here.
class FoodsModel(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.CharField(max_length=50)
