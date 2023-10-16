from django.db import models

# Create your models here.
# 5433


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=100, blank=True)
    password2 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
