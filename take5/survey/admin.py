from django.contrib import admin
from survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
    SurveyUserAnswer
)

# Register your models here.


admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAlternative)
admin.site.register(SurveyUserAnswer)
