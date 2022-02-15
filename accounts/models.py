from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):
    def create_user(self, email, password, name, phone, address):
        if not email:
            raise ValueError('New user must have an email!')
        if not name:
            raise ValueError('New user must have a name!')
        if not password:
            raise ValueError('New user must have a password!')
        if not phone:
            raise ValueError('New user must have a phone number!')

        user = self.model(
            email = self.normalize_email(email),
            password = password,
            name = name,
            phone = phone,
            address = address
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password, name, phone, address):

        #call the create user func. dont need to repeat the creating user process
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone=phone,
            address=address
        )

        #alter the attribute, so the user is recognized as admin in system
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=255)

    # Required fields for custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name', 'phone']
    objects = AccountManager()

    def __str__(self) -> str:
        return self.name

