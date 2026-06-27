from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SUPERVISOR = "SUPERVISOR", "Supervisor"
    ENGINEER = "ENGINEER", "Engineer"
    TECHNICIAN = "TECHNICIAN", "Technician"


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.TECHNICIAN,
    )

    def __str__(self):
        return self.username