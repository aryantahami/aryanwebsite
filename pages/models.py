from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.title}:{self.author}'
