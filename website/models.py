from django.db import models

class Warns(models.Model):
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.name
