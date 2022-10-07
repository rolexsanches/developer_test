from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializers import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer
from survey.models import Survey

# Create your views here.

class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Survey.objects.prefetch_related('questions')
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

