from django.db import models

# Create your models here.
class Book(models.Model):
    Bookname = models.CharField(max_length=100)
    Bookauthor = models.CharField(max_length=100)
    Bookpage = models.BigIntegerField()
    Bookprice = models.IntegerField()

    class Meta:
        db_table = 'Book'