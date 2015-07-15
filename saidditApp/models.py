from django.db import models

# Create your models here.

class Post(models.post):
    title = models.CharField(max_length=64)
    content = models.TextField()
    score = models.IntegerField()
    subreddit = models


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    birthday = models.DateField()

    gender = models.IntegerField(choices=(
        (1, "Male"),
        (2, "Female"),
        (3, "Other"),
    ))

    email = models.EmailField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Poll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person)
    question = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s (asked by %s)' % (self.question, self.creator)


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s asked in %s' % (self.choice, self.poll)


class PollVote(models.Model):
    class Meta:
        unique_together = ('creator', 'poll')

    created = models.DateTimeField(auto_now_add=True)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(PollChoice)
    creator = models.ForeignKey(Person)