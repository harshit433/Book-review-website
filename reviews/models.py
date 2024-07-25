from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.book.title} - {self.reader.username}'
