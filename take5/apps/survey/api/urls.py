from django.urls import include, path
from rest_framework import routers

from .views import SurveyViewSet, SurveyQuestionViewSet, SurveyQuestionAlternativeViewSet


app_name = "survey"

router = routers.DefaultRouter()
router.register('surveys', SurveyViewSet)
router.register('surveys-questions', SurveyQuestionViewSet)
router.register('surveys-questions-alternatives', SurveyQuestionAlternativeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]