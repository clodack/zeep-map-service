from django.db import models

class Objects(models.Model):
    lantitude = models.TextField()
    longitude = models.TextField()
    types = models.TextField()
    name = models.TextField() 