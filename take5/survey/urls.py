from django.urls import path
import survey.views as views

urlpatterns = [
    path('surveys/', views.surveys)
]
