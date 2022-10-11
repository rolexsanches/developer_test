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
    search_fields = ('question', 'survey__title')
    list_filter = ('survey__title',)


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ('alternative', 'question')
    search_fields = ('alternative', 'question__question')
    list_filter = ('question__question',)


@admin.register(SurveyUserAnswer)
class SurveyUserAnswerAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in SurveyUserAnswer._meta.get_fields()]
    readonly_fields = ('created', 'updated',)
    search_fields = ('user__username', 'survey__title',
                     'question__question', 'alternative__alternative')
    list_filter = ('user__username', 'survey__title',
                   'question__question', 'alternative__alternative')
