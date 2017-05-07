from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.title
