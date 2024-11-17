from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Quiz(models.Model):
    quiz_id = models.CharField(max_length = 10, unique= True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank= True, null= True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, to_field='id', on_delete=models.CASCADE, default=0, related_name= 'questions') 
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=30)
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.user.username} answered:{self.question.text} with{self.selected_choice.text}'
