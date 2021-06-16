from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) #separately because password needs to be encrypted
        user.save(using=self._db) #using... is to support multiple databases
        #create profile
        return user

    def create_superuser(self, email, password=None): #no worry about extra fields, as it is created by command line
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=264, unique=True) #unique so to create one user for one email
    firstName = models.CharField(max_length=264)
    lastName = models.CharField(max_length=264)
    is_active = models.BooleanField(default=True) #is user is active/online or not
    is_staff = models.BooleanField(default=False) #if staff, create user with special command

    objects = UserManager()

    USERNAME_FIELD = 'email'