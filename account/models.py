from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserBase(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(_('email address'), unique=True)
    user_name=models.CharField(max_length=150, unique=True)
    is_active= models.BooleanField(default=False)

    class Meta:
        verbose_name= "Accounts"
        verbose_name_plural= "Accounts"

    def __str__(self):
        return self.user_name

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
    
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

