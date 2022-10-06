from django.contrib.auth.models import User
from django.db import models


class Survey(models.Model):
    """Model: Pesquisa"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    """Model: questões"""
    survey = models.ForeignKey(
        Survey, related_name='questions', on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class SurveyQuestionAlternative(models.Model):
    """Model: alternativas"""
    question = models.ForeignKey(
        SurveyQuestion, related_name='alternatives', on_delete=models.CASCADE
    )
    alternative = models.CharField(max_length=255)

    def __str__(self):
        return self.alternative


class SurveyUserAnswer(models.Model):
    """Model: respostas do usuário"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user_answer = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_answer