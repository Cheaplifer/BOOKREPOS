import datetime
from django.db import models
from django.utils import timezone


class Author(models.Model):
    Author_name = models.CharField(max_length = 20)
    def __str__(self):
        return self.Author_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete= models.CASCADE)
    def __str__(self):
        return self.book_name
