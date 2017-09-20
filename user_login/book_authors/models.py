from django.db import models


class Books(models.Model):
    """Books in database."""
    name = models.CharField(max_length=60)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    """Authors of books."""
    books = models.ManyToManyField(
        'Books',
        related_name='authors'
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
