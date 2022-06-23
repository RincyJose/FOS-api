from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import filters
from rest_framework.filters import OrderingFilter
# from django_filters import rest_framework as filters


class QuestionsAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    

# filtering
# class QuestionsAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fields = ('question_text','author')
#     serializer_class = QuestionSerializer
    
# Search filter    
# class QuestionsAPIView(generics.ListCreateAPIView):
#     search_fields = ['question_text']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer    