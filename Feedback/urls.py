
from django.urls import path

from . import views
from knox import views as knox_views
urlpatterns = [
    path('api/addonefeedback/', views.FeedbackCreateView.as_view()),
    path('api/addfeedback/', views.FeedbackListCreateView.as_view()),
    path('api/viewfeedback/<int:pk>', views.FeedbackDetailView.as_view()),
    path('api/allfeedback/', views.FeedbackListDetailView.as_view() ,),
    path('api/deletefeedback/<int:pk>/', views.FeedbackListDeleteView.as_view()),
    path('api/updatefeedback/<int:pk>/', views.FeedbackListUpdateView.as_view()), # localhost:8000/api/
    
]