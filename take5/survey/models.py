from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    published_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, related_name='survey_questions',on_delete=models.CASCADE)
    survey_question = models.TextField(max_length=500)

    def __str__(self):
        return self.survey_question


class SurveyQuestionAlternative(models.Model):
    CHOICES = (
        ('A', 'Alternativa A'),
        ('B', 'Alternativa B'),
        ('C', 'Alternativa C'),
        ('D', 'Alternativa D'),
        ('E', 'Alternativa E'),
    )

    survey_question = models.ForeignKey(SurveyQuestion, related_name='survey_alternatives',on_delete=models.CASCADE)
    survey_alternative = models.CharField(max_length=255)
    survey_choice_alternative = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.survey_choice_alternative
        

class SurveyUserAnswer(models.Model):
    CHOICES = (
        ('A', 'Alternativa A'),
        ('B', 'Alternativa B'),
        ('C', 'Alternativa C'),
        ('D', 'Alternativa D'),
        ('E', 'Alternativa E'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField(max_length=1, choices=CHOICES)
    submited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_answer