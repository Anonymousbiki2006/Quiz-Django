from django.contrib import admin
from .models import Question,Choice,UserAnswer,Quiz

# Register your models here.

admin.site.register(Question)
admin.site.register(UserAnswer)
admin.site.register(Choice)
admin.site.register(Quiz)