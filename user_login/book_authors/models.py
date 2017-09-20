from django.db import models


class Books(models.Model):
    """Books in database."""

    liked_users = models.ManyToManyField(
        'users',
        related_name='liked_books',
        null=True,
    )
    uploader = models.ForeignKey(
        'users',
        related_name='uploaded_books',
        null=True,
    )
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


class users(models.Model):
    """Users on book site."""
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)