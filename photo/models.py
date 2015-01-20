from django.conf import settings
from django.db import models


class Gallery(models.Model):
    dir_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    summary = models.TextField()


class Image(models.Model):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=8)
    gallery = models.ForeignKey(Gallery)

    @property
    def tn_src(self):
        return "/static/%s/tn/%s.%s" % (self.gallery.dir_name, self.filename, self.extension)

    @property
    def src(self):
        return "/static/%s/%s.%s" % (self.gallery.dir_name, self.filename, self.extension)
