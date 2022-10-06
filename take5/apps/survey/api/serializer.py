from asyncore import read
from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Survey, SurveyQuestion, SurveyQuestionAlternative


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = ('__all__')


class SurveyQuestionSerializer(serializers.ModelSerializer):
    alternatives = SurveyQuestionAlternativeSerializer(many=True, read_only=True)
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'question', 'survey', 'alternatives']


class SurveySerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = [
            'id', 'title', 'description', 'author', 'created',
            'updated', 'is_active', 'questions'
        ]
