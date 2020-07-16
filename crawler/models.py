from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    """
     Database table where all the scraped articles are saved for the listview and many other purpose.
    """

    # Below variables will be the coloums name in the database of the table named
    # as Artile
    # The class name will be the database table name in databse.
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200,)
    abstract = models.TextField(max_length=600)
    pdf_link = models.URLField()
    date = models.CharField(max_length=200, null=True)
    searched = models.DateTimeField(default=timezone.now)

    # Here we are just adding the string represntation of our model
    # So that we can easily read this in table, By default Django will save this
    # in objects forms, Because in python we know everything is object.

    def __str__(self):
        return self.title
