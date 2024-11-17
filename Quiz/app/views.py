from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core import serializers
from .models import Question,Choice,Quiz
from .forms import QuestionForm,ChoiceForm,UserAnswerForms,UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Question added successfully")
            return redirect('question_list')
            
        else:
            form = QuestionForm()

        return render(request, 'add_question.html', {'form':form})
    

@login_required
def add_choice(request,question_id):
    question = get_object_or_404(Question, id = question_id)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit = False)
            choice.question = question
            choice.save()
            messages.success(request, "Choices added successfully")
            return redirect('question_detail', question_id = question.id)

        else:
            form = ChoiceForm()

        return render(request, 'add_choices.html',{'form':form, 'question':question}) 


def user_answer(request, question_id):
    questions = get_object_or_404(Question, id= question_id)
    user = request.user

    if request.method == 'POST':
        form = UserAnswerForms(request.POST)
        if form.is_valid():
            user_answer = form.save(commit= False)
            user_answer.user = user
            user_answer.question = questions
            user_answer.save()
            messages.success(request,"Answer submitted successfully")
            return redirect('question_list')

        else:
            form = UserAnswerForms(initial={'user':user, 'question':questions})

        
        return render(request,'submit_quiz.html', {'form':form, 'question': questions})


def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id = quiz_id)
    questions = quiz.questions.prefetch_related()
    return render(request, 'quiz_view.html', {'quiz':quiz,'questions':questions})

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# View the list of all the questions
@login_required
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions':questions})

#View the details of a single question along with it's choices
@login_required
def question_detail(request,question_id):
    questions = get_object_or_404(Question, id=question_id)
    choices = Choice.objects.filter(question = questions)
    return render(request, 'question_detail.html',  {'question':questions, 'choices': choices})


def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id= quiz_id)
    if request.method == 'POST':
        messages.success(request, 'Quiz submitted successfully')
        return render(request, 'submit_quiz.html', {'quiz': quiz})
    else:
        return redirect('quiz_view', quiz_id = quiz_id)