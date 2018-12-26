from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from questions.forms import EditProfileForm
from django.views.generic.list import ListView
from questions.models import Question
from django.contrib.auth import update_session_auth_hash

class QuestionListView(ListView):
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            is_starred = False                                                  #Move to question_detail view
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

        if question.starred.filter(id=request.user.id).exists():                  #Move to question_detail view
            is_starred = True

        context = {
            'is_starred': is_starred,                                           #Move to question_detail view
        }

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


def question_starred_list(request):
    user = request.user
    starred_questions = user.starred.all()
    context = {
        'starred_questions': starred_questions,
    }
    return render(request, 'profile/question_starred_list.html', context)

def starred_question(request, id):                                      
    question = get_object_or_404(Question, id=id)                       
    if question.starred.filter(id=request.user.id).exists():              
        question.starred.remove(request.user)                             
    else:        
        question.starred.add(request.user)                                
    return HttpResponseRedirect(question.get_absolute_url())            
