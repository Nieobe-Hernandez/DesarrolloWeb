from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.db import models
from django.utils.timezone import now

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, surname, age, tel, control_number, address, **extra_fields):
       if not email:
           raise ValueError('El correo electrónico es obligatorio')
       email = self.normalize_email(email)
       user = self.model(email=email, **extra_fields)
       user.set_password(password)
       user.name = name
       user.surname = surname
       user.age = age
       user.tel = tel
       user.control_number = control_number
       user.address = address
       user.save(using=self._db)
       return user
   
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(unique=True)
   token = models.CharField(max_length=255, blank=True, null=True)
   name = models.CharField(max_length=100)
   surname = models.CharField(max_length=100)
   control_number = models.CharField(max_length=20, unique=True)
   age = models.PositiveIntegerField()
   tel = models.CharField(max_length=15)
   address = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo
   join_date = models.DateTimeField(default=now)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   
   objects = CustomUserManager()
   
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['name', 'surname', 'control_number', 'age', 'tel', 'gener']

   def __str__(self):
       return self.email