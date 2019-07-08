from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps django work with our custom model"""

    # tells django how to create user from our Userprofile
    def create_user(self, email, name, password):
        """Creates a new user profile object"""

        # logic that creates a new user in the system
        # first check if email was provided
        if not email:
            raise ValueError("Users must have an email address")

        # normalizing email address(converts all characters to lowercase, and doamin name too)
        email = self.normalize_email(email)

        # Create new user object
        user = self.model(email=email, name=name)

        # set user password (set_password will encrypt password)
        user.set_password(password)

        # save
        user.save(using=self._db)

        return user

    # How to create a super user
    def create_superuser(self, email, name, password):
        """Creates and saves a super user with given details"""
        user = self.create_user(email, name, password)

        # assign 2 vars to the user, set is_super_user and is_staff to true
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


# substituting custom user model (django)
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system."""

    # fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # manages the user profiles and define admin/regular user
    objects = UserProfileManager()

    # username_field is what users use to log in
    USERNAME_FIELD = 'email'

    # required fields
    REQUIRED_FIELDS = ['name']  # could be as many as possible

    # helper functions
    def get_full_name(self):
        """Used to get a user full name
        """
        return self.name

    # return first name only
    def get_short_name(self):
        """Used to get a user short name"""
        return self.name

    def __str__(self):
        """Required django function, so it knows how to return
        objects as string, convert objects to string
        """
        return self.email
