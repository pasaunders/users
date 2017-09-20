from django.db import models

# Create your models here.
class dojo(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    desc = models.TextField(max_length=500)


class ninjas(models.Model):
    dojo = models.ForeignKey(
        'dojo',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
