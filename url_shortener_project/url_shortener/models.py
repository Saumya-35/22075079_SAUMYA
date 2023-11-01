from django.db import models

class URLMapping(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
