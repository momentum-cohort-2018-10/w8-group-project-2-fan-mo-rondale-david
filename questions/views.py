from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from questions.forms import EditProfileForm
from django.views.generic.list import ListView
from questions.models import Question
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class QuestionListView(ListView):
    paginate_by = 10
    template_name = 'index.html'
    queryset = Question.objects.all()


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change_password.html', args)
