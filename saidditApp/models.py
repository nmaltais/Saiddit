from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subsaiddit(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

# USING DJANGO'S USER MODEL. FROM django.contrib.auth.models tO USE THE AUTHENTICATE(), LOGIN() & LOGOUT()
#class User(models.Model):
#    username = models.CharField(max_length=64)
#    password = models.CharField(max_length=64)
#
#    def __unicode__(self):
#        return u'%s' % self.username


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    score = models.IntegerField()
    subsaiddit = models.ForeignKey(Subsaiddit)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Title:%s by:%s on %s' % (self.title, self.user, self.subsaiddit)


class Comment(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return u'%s (Author:%s on post:%s)' % (self.content, self.user, self.post)