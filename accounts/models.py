from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='jobseeker'
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

