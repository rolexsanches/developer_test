# encoding: utf-8

from django.contrib.auth import get_user_model

from apps.survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative

# criando um usuário
User = get_user_model()
user = User.objects.create(
    username='pesquisador',
)

user.set_password('survey@2022')
user.save()

# Criando uma Pesquisa
survey = Survey.objects.create(
    title='Linguagem de Programação',
    description='Pesquisa da linguagem de programação mais utilizada.',
    author=user,
)

# Criando as Questões da pesquisa
questions = [
    'Qual linguagem você mais gosta?',
    'Qual linguagem você trabalha?',
    'Qual linguagem você está estudando?',
]
for question in questions:
    SurveyQuestion.objects.create(
        survey=survey,
        question=question,
    )

# Criando as alternativas
alternatives = ['Python', 'JavaScript', 'C#']
questions = SurveyQuestion.objects.filter(survey=survey)
for question in questions:
    for alternative in alternatives:
        SurveyQuestionAlternative.objects.create(
            question=question,
            alternative=alternative
        )
