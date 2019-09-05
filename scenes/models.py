from django.db import models

class Scene(models.Model):
    id = models.IntegerField('场景ID', primary_key=True)

