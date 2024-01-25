from django.db import models

# Create your models here.

from django.db import models
from geonode.base.models import HierarchicalKeyword

class HomeCollection(models.Model):
    
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    material_icon = models.CharField(max_length=128, blank=True, null=True)
    link_type = models.CharField(max_length=128 ,choices=[('keywords', 'Keywords'), ('external', 'External')])
    url = models.CharField(max_length=128, unique=True, blank=True, null=True)
    keywords = models.ManyToManyField(HierarchicalKeyword, blank=True)

    def __str__(self):
        return self.name