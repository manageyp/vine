from django.db import models

class User(models.Model):
    id = models.IntegerField('用户ID', primary_key=True)

