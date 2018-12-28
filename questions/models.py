from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, EmailMultiAlternatives


class User(AbstractUser):

    USERNAME_FIELD = 'username'


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class StarredItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stars')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ("user", "object_id", "content_type")

    def __str__(self):
        return f'({self.user}), ({self.content_type} - {self.object_id})'


class Question(Timestamp):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    stars = GenericRelation(StarredItem, related_query_name="question_stars")

    def __str__(self):
        return self.title


class Answer(Timestamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, related_name='answers')
    stars = GenericRelation(StarredItem)

    def __str__(self):
        return f'{self.text[:20]}...'


class Resolve(Timestamp):
    resolved_question = models.OneToOneField(
        Question, on_delete=models.CASCADE, related_name='resolved')
    resolving_answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE, related_name='resolved_answer')

    def clean(self):
        self.resolved_question
        answerset = Answer.objects.filter(question=self.resolved_question)
        if self.resolving_answer not in answerset:
            raise ValidationError(
                _("Resolved answers must be already be "
                  "in a question's set of answers."))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username} Profile'
