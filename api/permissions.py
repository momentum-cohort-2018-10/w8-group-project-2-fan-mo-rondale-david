from rest_framework import permissions
from questions.models import Question


class OnlyAuthorCanMarkResolved(permissions.BasePermission):
    """
    Only question authors can mark an answer as resolved
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        question = Question.objects.get(pk=view.kwargs['pk'])

        return question.author == request.user

    def has_object_permission(self, request, view, resolve):
        if request.method in permissions.SAFE_METHODS:
            return True

        return resolve.resolved_question.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only question authors can delete their posts
    """

    def has_object_permission(self, request, view, question):
        if request.method in permissions.SAFE_METHODS:
            return True

        return question.author == request.user


class IsStarOwnerOrReadOnly(permissions.BasePermission):
    """
    Only original star owners can remove the star
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsAnswerOwnerOrReadOnly(permissions.BasePermission):
    """
    Only answer owners can delete their responses
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
