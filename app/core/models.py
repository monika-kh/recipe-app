from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_field):
		user = self.model(email=email, **extra_field)
		user.set_password(password)
		user.save(using=self._db)

		return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    object = UserManager()
    USERNAME_FIELD = "email"