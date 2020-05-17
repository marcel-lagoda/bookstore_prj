import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=260)
    author = models.CharField(max_length=260)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    review = models.TextField(max_length=355)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review

