from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from survey.views import SurveyQuestionAlternativeViewSet, SurveyQuestionViewSet, SurveyViewSet


router = routers.DefaultRouter()
router.register('survey', SurveyViewSet)
router.register('survey-question', SurveyQuestionViewSet)
router.register('survey-alternatives', SurveyQuestionAlternativeViewSet )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
