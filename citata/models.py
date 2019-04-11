from django.db import models

class Quote(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)

    def __str__(self):
        return self.title
