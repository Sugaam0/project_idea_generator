from django.db import models
from django.contrib.auth.models import AbstractUser
from account.managers import CustomUserManager
# Create your models here.

Gender = (
    ('M', "Male"),
    ('F', "Female"),

)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    gender = models.CharField(choices=Gender, max_length=1)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    objects = CustomUserManager()