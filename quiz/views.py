from django.shortcuts import render, get_object_or_404
from .models import Quiz, UserQuiz, Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quiz_list': quizzes})


@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.corret_answer:
                score += 1

        user_quiz = UserQuiz.objects.create(quiz=quiz, user=request.user, score=score)
        return render(request, 'quiz/quiz_result.html', context={'score': score, 'quiz': quiz, 'questions': questions.filter(quiz=quiz).count()})

    return render(request, 'quiz/quiz_detail.html', context={'quiz': quiz, 'questions': questions})
