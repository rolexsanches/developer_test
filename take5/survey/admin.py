from django.contrib import admin
from survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
    SurveyUserAnswer
)

# Register your models here.


admin.site.register(Survey)


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'survey')


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ('alternative', 'question')


@admin.register(SurveyUserAnswer)
class SurveyUserAnswerAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in SurveyUserAnswer._meta.get_fields()]
    readonly_fields = ('created', 'updated',)
