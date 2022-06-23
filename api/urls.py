from django import views
from django.urls import re_path
from api.views import QuestionsAPIView
from django.contrib.auth import views as as_view
from rest_framework.views import APIView

urlpatterns = [
    re_path('questions',QuestionsAPIView.as_view())
]