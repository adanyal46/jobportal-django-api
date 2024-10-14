from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .custom_user_manager import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=False, null=True, blank=True) 
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('mentor', 'Mentor'),
        ('recruiter', 'Recruiter'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(
        upload_to='profiles/',
        null=False,
        blank=False,
        default="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
