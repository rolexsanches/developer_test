from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    survey_question = models.TextField(max_length=500)

    def __str__(self):
        return self.survey_question


class SurveyQuestionAlternative(models.Model):
    CHOICES = (
        ('A','Alternativa A'),
        ('B','Alternativa B'),
        ('C','Alternativa C'),
        ('D','Alternativa D'),
        ('E', 'Alternativa E')
    )

    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    survey_alternative = models.CharField(max_length=255)
    survey_choice_alternative = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.survey_alternative

class SurveyUserAnswer(models.Model):
    CHOICES = (
        ('A', 'Alternativa A'),
        ('B', 'Alternativa B'),
        ('C', 'Alternativa C'),
        ('D', 'Alternativa D'),
        ('E', 'Alternativa E')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1, choices=CHOICES)


    def __str__(self):
        return self.user_answer