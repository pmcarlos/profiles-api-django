from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
  """Helps Django work with our custom user model"""

  def create_user(self, email, name, password):
    """Creates new user profile object"""

    if not email:
      raise ValueError('Users must have a email address')
    
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_super_user(self, email, name, password):
    """Creates a super user"""

    user = self.create_user(email=email, name=name, password=password)

    user.is_super_user = True
    user.is_staff = True

    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Represents a "user Profile" inside our system"""

  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """Gets a users full name"""

    return self.name

  def get_short_name(self):
    """Gets a users short name"""

    return self.name

  def __str__(self):
    """Used by django to convert object to string"""

    return self.email