from django.db import models
from django.utils import timezone as tz

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=4000)
    date_created = models.DateTimeField(default=tz.now)
    date_published = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.date_published = tz.now()

    def __str__(self):
        return self.title
