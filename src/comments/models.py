from django.db import models
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    """Documentation for ClassName

    """
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=20)

    def __unicode__(self):
        return self.text
