from .models import CustomUser
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
#serializador para los tokens
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        #se pueden agregar mas campos
        # token['name'] = user.name
        # token['surname'] = user.surname
        # token['control_number'] = user.control_number
        # token['age'] = user.age
        # token['tel'] = user.tel
        return token