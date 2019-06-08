from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class BooksInformation(models.Model):
    book = models.ForeignKey(Books, default=None, on_delete=models.CASCADE)
    about_book = models.TextField()
    author = models.CharField(max_length=200)
    edition = models.PositiveIntegerField()
    isbn_number = models.PositiveIntegerField()


    def __str__(self):
        return  self.about_book
    