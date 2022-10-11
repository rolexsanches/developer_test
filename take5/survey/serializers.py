from rest_framework import serializers
from survey.models import (Survey, SurveyQuestion, SurveyQuestionAlternative)


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = ['alternative']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    alternatives = SurveyQuestionAlternativeSerializer(
        many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ['question', 'alternatives']


class SurveySerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['title', 'questions']
