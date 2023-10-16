from django.db import models
from datetime import datetime

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()

    def __str__(self):
        return self.title
