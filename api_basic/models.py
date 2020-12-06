from django.db import models

# Create your models here.

class Alien(models.Model):
    """
    Classified extraterrestrial creatures
    """
    name            = models.CharField( max_length=100)
    planet          = models.CharField( max_length=100)
    solarSystem     = models.CharField( max_length=100)
    dateDiscovered  = models.DateField( auto_now_add=True)
    email           = models.EmailField(max_length=100)
    color           = models.CharField( max_length=100)
    size            = models.IntegerField()
    category        = models.CharField( max_length=100)
    def __str__(self):
        return self.name


class Box(models.Model):
    """
    For that crud react example
    """
    name        = models.CharField(max_length=100)
    location    = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight      = models.IntegerField()
    def __str__(self):
        return self.name
