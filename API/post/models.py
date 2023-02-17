from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=20, unique=True, blank=False)
    slug = models.SlugField(blank=True)
    content = models.TextField(max_length=1500)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def count_likes(self):
        return self.likes.all().count()
