from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    _status = (
        ('opn', 'Open', ),
        ('cls', 'Close', ),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    status = models.CharField(max_length=20, choices=_status, default='opn')
    image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.content)

class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.name)
