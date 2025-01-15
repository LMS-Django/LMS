from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **kwargs):
#         email = self.normalize_email(email)
#         user = self.model(email=email, **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if not extra_fields.get('is_staff'):
#             raise ValueError('Superuser must have is_staff=True.')
#         if not extra_fields.get('is_superuser'):
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, blank=False, max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Изменение имени обратной связи для групп
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Изменение имени обратной связи для разрешений
        blank=True,
    )
