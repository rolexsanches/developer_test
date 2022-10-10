from rest_framework import serializers

from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = SurveyQuestionAlternative
        fields = ['id', 'survey_question', 'survey_alternative', 'survey_choice_alternative']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    survey_alternatives = SurveyQuestionAlternativeSerializer(many=True, read_only=True)
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'survey', 'survey_question', 'survey_alternatives']


class SurveySerializer(serializers.ModelSerializer):
    survey_questions = SurveyQuestionSerializer(many=True, read_only=True) 
    class Meta:
        model = Survey
        fields = ['id','title', 'description', 'published_at','survey_questions']



