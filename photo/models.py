from django.db import models


class Gallery(models.Model):
    dir_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    summary = models.TextField()
