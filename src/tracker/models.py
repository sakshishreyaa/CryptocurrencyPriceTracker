from django.db import models

# Create your models here.
class CryptoTracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    latest = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
