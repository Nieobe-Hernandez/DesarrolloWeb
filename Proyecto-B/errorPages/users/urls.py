from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = SimpleRouter()
router.register(r'api', UserViewSets) #get, post, put, delete

urlpatterns = [
   path('', include(router.urls)),
   #Este es el path para iniciar sesion <- requiere email y password
   path('token/', CustomTokenObtainPairView.as_view(), name='token'),
   path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]

