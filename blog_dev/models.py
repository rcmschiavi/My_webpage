from django.db import models
from django.urls import reverse


class Keyword(models.Model):
    keyword = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.keyword)

    def get_absolute_url(self):
        return reverse('open_keyword', {'slug': self.keyword})


class Blog_en(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, default=" ")
    url = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return 'Title: ' + str(self.title)

    def return_post(self):
        return {'Title': str(self.title), 'body': str(self.body)}

    def get_absolute_url(self):
        return self.url

