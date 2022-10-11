from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    question = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'


class SurveyQuestionAlternative(models.Model):
    alternative = models.TextField()
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alternative}'


class SurveyUserAnswer(models.Model):
    """
    Bom aqui eu pensei em três possíveis soluções:

    1ª Opção:
    Esse modelo tem um campo answers que recebe todas as respostas 
    serializadas (binaria ou pickle) de alguma forma assim reduzindo o número de 
    instancias mas isso adicionaria mais um passo caso o objetivo seja 
    analisar os dados alternativa por alternativa posteriormente.

    2ª Opção
    O jeito óbvio e mais simples de fazer uma instância do modelo por
    alternativa e resposta. 


    Uma terceira opção também seria adicionar mais um modelo pra cada alternativa
    e transformando esse modelo atual (SurveyUserAnswer) em um agrupamento de todas 
    as respostas por survey e usuario mas como foi especificado para criar os 
    4 modelos apenas, optei pela segunda opção.
    """
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    alternative = models.ForeignKey(
        SurveyQuestionAlternative, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'
