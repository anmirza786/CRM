from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from .roles_models import Role


class UserAccountManager(UserManager):

    def create_superuser(self, email, first_name, last_name, password=None):
        ADMIN_ROLE = Role.objects.filter(name="Global Administrator").first()
        if not email:
            raise ValueError('User must has an email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.role = ADMIN_ROLE
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

    def create_user(self, email, first_name, last_name, password=None):
        INDIVIDUAL_ROLE = Role.objects.filter(name="Individual").first()
        if not email:
            raise ValueError('User must has an email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.role = INDIVIDUAL_ROLE
        user.save()
        return user


class UserAccount(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(
        max_length=255, unique=False, blank=True, null=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    role = models.ForeignKey(
        Role, on_delete=models.SET_DEFAULT, default=1, null=False, blank=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
