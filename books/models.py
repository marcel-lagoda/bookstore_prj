from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=260)
    author = models.CharField(max_length=260)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


