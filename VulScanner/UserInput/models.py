from django.db import models

class Asset(models.Model):
    asset_name = models.CharField(max_length=50)
    asset_version = models.CharField(max_length=50)
    
    def __str__(self):
      return self.asset_name + "--" + self.asset_version