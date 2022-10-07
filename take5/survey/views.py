from rest_framework import viewsets

from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative
from survey.serializers import SurveyQuestionAlternativeSerializer, SurveyQuestionSerializer, SurveySerializer


class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all() 
    serializer_class = SurveySerializer

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    
    queryset = SurveyQuestion.objects.prefetch_related('survey').all()
    serializer_class = SurveyQuestionSerializer 


class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    
    queryset = SurveyQuestionAlternative.objects.prefetch_related('survey_question').all()
    serializer_class = SurveyQuestionAlternativeSerializer


