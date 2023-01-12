from django.shortcuts import render
from rest_framework import generics,permissions,authentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
        
        
        
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
@api_view(('GET',))
def Userdata(request):
    if request.user.is_authenticated:
        print("Autheticated")
        print(request.user.username)
        print(request.user.id)
    
        
        
    return JsonResponse({'id':request.user.id,'username':request.user.username,'email':request.user.email,'is_superuser':request.user.is_superuser})
    
    
    
    
    
    
    
    








class ProductCreateView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProductDetailView(generics.RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # Can only access after login
    # permission_classes = [permissions.IsAuthenticated]

    
    
    
class ProductListDetailView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
 
    
    
class ProductListDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication]
  
    
    
class ProductListUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # Can only access after login
    # authentication_classes=[authentication.SessionAuthentication]
    
# Create your views here.
