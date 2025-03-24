from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)  # Ensure ISBN is unique
    published_date = models.DateField()

    def __str__(self):
        return self.title