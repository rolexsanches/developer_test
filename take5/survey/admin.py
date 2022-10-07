from django.contrib import admin

from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer

# Register your models here.

admin.site.register([Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer])
