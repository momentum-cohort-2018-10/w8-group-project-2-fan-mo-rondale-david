from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'username'


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Question(Timestamp):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


class Answer(Timestamp):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
