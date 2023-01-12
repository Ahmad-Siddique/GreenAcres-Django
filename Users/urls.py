from .views import RegisterAPI
from django.urls import path
from .views import LoginAPI
from . import views
from knox import views as knox_views
urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/<int:pk>/', views.ProductDetailView.as_view() , name='detailview'),
    path('api/detailview/', views.ProductListDetailView.as_view()),
    path('api/update/<int:pk>/', views.ProductListUpdateView.as_view()), # localhost:8000/api/
    path('api/delete/<int:pk>/', views.ProductListDeleteView.as_view()), # localhost:8000/api/
    path('api/userdata/', views.Userdata), # localhost:8000/api/
]