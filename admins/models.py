from django.db import models

class Header(models.Model):
    header = models.CharField(max_length=200)

    def __str__(self):
        return self.header