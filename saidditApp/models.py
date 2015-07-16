from django.db import models

# Create your models here.

class Subreddit(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    score = models.IntegerField()
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Title:%s by:%s on %s' % (self.title, self.user, self.content)


class Comment(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return u'%s (Author:%s on post:%s)' % (self.content, self.user, self.post)