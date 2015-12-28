from __future__ import unicode_literals


from django.db import models


class Post(models.Model):
    name = models.CharField('Post', max_length = 100)

class Comment(models.Model):
    Post = models.ForeignKey(Post)

    comment = models.CharField('Comentario', max_length = 200)
