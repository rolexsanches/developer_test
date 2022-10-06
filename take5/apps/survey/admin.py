from django.contrib import admin

from .models import Survey, SurveyQuestion, SurveyQuestionAlternative


class QuestionInline(admin.TabularInline):
    model = SurveyQuestion
    extra = 0


class AlternativeInline(admin.TabularInline):
    model = SurveyQuestionAlternative
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated', 'is_active']
    inlines = [QuestionInline]


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'survey']
    inlines = [AlternativeInline]


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ['alternative', 'question']
