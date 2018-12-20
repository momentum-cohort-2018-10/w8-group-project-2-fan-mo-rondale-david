from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class User(AbstractUser):

    USERNAME_FIELD = 'username'


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class StarredItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='stars')
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type',
                                       'object_id')

    class Meta:
        unique_together = ("user", "object_id", "content_type")


class Question(Timestamp):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    stars = GenericRelation(StarredItem, related_query_name="question_stars")


class Answer(Timestamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='answers')
    stars = GenericRelation(StarredItem)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username} Profile'