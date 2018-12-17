from django.contrib import admin
from questions.models import User, Question, Answer, StarredItem
from django.contrib.auth.admin import UserAdmin



class QuestionAdmin(admin.ModelAdmin):

    model = Question
    list_display = ['title', 'author', 'text']


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ['author', 'text']


class StarredItemAdmin(admin.ModelAdmin):
    model = StarredItem
    list_display = ['user', 'content_type', 'object_id', 'content_object']


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(StarredItem, StarredItemAdmin)
