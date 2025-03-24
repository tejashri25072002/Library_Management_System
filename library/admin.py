from django.contrib import admin
from .models import Admin, Book
# Register your models here.
admin.site.register(Book)

admin.site.register(Admin)