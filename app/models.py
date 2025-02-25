from django.db import models

# Create your models here.

class amount(models.Model):
    Amount = models.IntegerField(null=False, blank=False)