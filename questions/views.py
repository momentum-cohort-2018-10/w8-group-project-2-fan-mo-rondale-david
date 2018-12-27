from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from questions.forms import EditProfileForm
from django.views.generic.list import ListView
from django.contrib.auth import update_session_auth_hash
from questions.models import Question, Answer
from django.contrib.contenttypes.models import ContentType


class QuestionListView(ListView):
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            question = ContentType.objects.get(model='question').id

            queryset = Question.objects.raw(
                'SELECT q.*, s.id AS star, u.username AS author_name '
                'from questions_question q '
                'LEFT JOIN (SELECT * FROM questions_starreditem '
                'WHERE content_type_id = %s and user_id = %s) '
                's ON q.id = s.object_id '
                'LEFT JOIN (SELECT u.id, u.username from questions_user u) '
                'u on q.author_id = u.id '
                'ORDER BY q.created_at DESC', (
                    question,
                    user_id
                    )).prefetch_related('answers').prefetch_related('resolved')

        else:
            queryset = Question.objects.all().prefetch_related('answers')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        answer = ContentType.objects.get(model='answer').id

        context['answers'] = Answer.objects.raw(
                'SELECT a.*, s.id AS star, u.username AS author_name '
                'from questions_answer a '
                'LEFT JOIN (SELECT * FROM questions_starreditem '
                'WHERE content_type_id = %s and user_id = %s) '
                's ON a.id = s.object_id '
                'LEFT JOIN (SELECT u.id, u.username from questions_user u) '
                'u on a.author_id = u.id', (
                    answer,
                    user_id
                    ))
        return context


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'profile/change_password.html', args)  
