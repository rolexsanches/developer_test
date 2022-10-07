from django.contrib import admin

from survey.models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer

# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Survey, SurveyAdmin)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'survey_question')

admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ('survey_question', 'survey_alternative', )

admin.site.register(SurveyQuestionAlternative, SurveyQuestionAlternativeAdmin)
class SurveyUserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'user_answer')

admin.site.register(SurveyUserAnswer, SurveyUserAnswerAdmin)

