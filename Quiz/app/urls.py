from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from app import views

urlpatterns = [
    
    path('', views.quiz_list, name = 'quiz_list'),   #homepage with avaiable Quizzes
    path('quizzes/', views.quiz_list, name = 'quiz_list'), 
    path('<int:quiz_id>/', views.quiz_view, name = 'quiz_view'), #Viewing a specific quiz
    path('question/<int:question_id>/', views.question_detail, name = 'question_detail'), #Specific question detail
    path('question/add/', views.add_question, name = 'add_question'), #add a question
    path('question/<int:question_id>/add_choice/', views.add_choice, name ='add_choice'), #add choice
    path('questionlist/', views.question_list, name = 'question_list'), #view all question
    path('<int:quiz_id>/submit/', views.submit_quiz, name = 'submit_quiz'),
    path('register/', views.register, name = 'register' ),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logged_out.html'), name = 'logout'),
    path('accounts/profile/', views.quiz_list, name = 'quiz_list '),

]