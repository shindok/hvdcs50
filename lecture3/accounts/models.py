from typing import Optional
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    # this list should be correspond with the CustomUser's fields
    allowed_fields = ['first_name', 'last_name', 'username','email', 'password']

    def create_user(self, username, password=None, **extra_fields):
        for field in extra_fields:
            if field not in self.allowed_fields:
                raise ValueError(f'Invalid field: {field}')
        
        email = self.normalize_email(extra_fields.get('email'))

        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        for field in extra_fields:
            if field not in self.allowed_fields:
                raise ValueError(f'Invalid field: {field}')
        
        email = self.normalize_email(extra_fields.get('email'))

        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
            
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

        # return self.create_user(username, password, **extra_fields) 
        # #TODO: refactor the code to limit repetition
    
    def validate_fields(self, **extra_fields):
        for field in extra_fields:
            if field not in self.allowed_fields:
                raise ValueError(f'Invalid field: {field}')
            
    

class CustomUser(AbstractBaseUser):
    #these fields should correspond with the allowed_fields in CustomUserManager
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True