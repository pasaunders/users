from django.db import models

class User(models.Model):
    """Create user model."""


    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_address = models.CharField(max_length=60)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)