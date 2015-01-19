from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)

    @property
    def summary(self):
        cutoff = 1024
        if len(self.body) < cutoff:
            return self.body
        else:
            return "%s..." % self.body[:cutoff]
