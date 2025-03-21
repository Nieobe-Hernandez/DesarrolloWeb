from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer

# Hacer las vistas del API REST de usuarios
class UserViewSets(viewsets.ModelViewSet):
    #3 variables que se deben de definir
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
## Si quieres agregar la parte de seguridad 
# pon estas 2 variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    #definir que metodos se van a proteger
    def get_permissions(self):
        if self.request.method in  ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []
    
#Hacer una vista que me devuelva mi Token
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer