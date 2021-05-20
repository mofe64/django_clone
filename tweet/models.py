from django.db import models


# Create your models here.
class Tweet(models.Model):
    tweet = models.TextField(max_length=140, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet
