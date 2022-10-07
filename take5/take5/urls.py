from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from survey.views import SurveyQuestionAlternativeViewSet, SurveyQuestionViewSet, SurveyViewSet


router = routers.DefaultRouter()
router.register('survey', SurveyViewSet, basename='Survey')
router.register('survey-question', SurveyQuestionViewSet, basename='Cursos')
router.register('survey-alternatives', SurveyQuestionAlternativeViewSet, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
