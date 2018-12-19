from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.list import ListView
from questions.models import Question


def index(request):
    return render(request, 'index.html')


class QuestionListView(ListView):
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Question.objects.all().prefetch_related('answers')
        return queryset


def register(request):
    """
    Redirects to home page upon successful user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registration_form.html', {
            'form': form
        })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('account_home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {
            'form': form
        })
