from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=220)
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    date_availability = models.DateTimeField()
    image = models.ImageField(upload_to="images")
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    