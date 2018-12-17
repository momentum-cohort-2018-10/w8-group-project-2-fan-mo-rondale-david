from django.contrib import admin
from questions.models import User, Question, Answer
from django.contrib.auth.admin import UserAdmin


class QuestionAdmin(admin.ModelAdmin):

    model = Question
    list_display = ['title', 'author', 'text']


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ['author', 'text']


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
