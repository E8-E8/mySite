from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Room(models.Model):
    name = CharField(max_length=200)
    