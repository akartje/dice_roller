from django.db import models

# Create your models here.
class DiceRoll(models.Model):
    roll = models.IntegerField()
    result = models.IntegerField()
    option = models.CharField(max_length=30, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)