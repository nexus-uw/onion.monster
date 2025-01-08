from datetime import datetime, timezone
from django.db import models

# Create your models here.
class Record(models.Model):
    domain = models.CharField(max_length=200)
    key = models.CharField(max_length=64,primary_key=True)
    lastUpdated = models.DateField()

