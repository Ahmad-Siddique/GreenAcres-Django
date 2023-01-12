from django.shortcuts import render
from rest_framework import generics,permissions,authentication

from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import FeedbackSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from .models import Feedback
    
    
    
    
    
    
    
    








class FeedbackCreateView(generics.CreateAPIView):
    
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    
    
class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer



class FeedbackDetailView(generics.RetrieveAPIView):
    
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    # Can only access after login
    permission_classes = [permissions.IsAuthenticated]

    
    
    
class FeedbackListDetailView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
 
    
    
class FeedbackListDeleteView(generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication]
  
    
    
class FeedbackListUpdateView(generics.UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication]
    
# Create your views here.
