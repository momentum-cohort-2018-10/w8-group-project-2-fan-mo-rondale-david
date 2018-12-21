from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from questions.models import Question


class QuestionListView(ListView):
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            queryset = Question.objects.raw(
                'SELECT q.*, s.id AS star '
                'from questions_question q LEFT JOIN '
                '(SELECT * FROM questions_starreditem '
                'WHERE content_type_id = 8 and user_id = %s) '
                's ON q.id = s.object_id', (user_id,)
                ).prefetch_related('answers')
        else:
            queryset = Question.objects.all().prefetch_related('answers')

        return queryset


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
