from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    # Multiple choice answers
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    corret_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class UserQuiz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
    national_id = models.CharField(max_length=10, primary_key=True, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    birth_date = models.DateField(null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['email', 'national_id', 'first_name', 'last_name']


    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
