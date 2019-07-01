from django.db import models

# Create your models here.
class Items (models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=200)