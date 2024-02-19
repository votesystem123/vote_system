from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

from django.utils import timezone

# Create your models here.
ROLE_CHOICES = (
    ("voter", "Voter"),
    ("admin", "Admin"),
)

class AiUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.role = "admin"
        user.is_staff = True
        user.save(using=self._db)
        return user

class AiUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default = 'voter')
    date_joined = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = AiUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    class Meta:
        verbose_name = "Ai User"
        verbose_name_plural = "Ai Users"

class Position(models.Model):
    position_name = models.CharField(max_length=100)

    def __str__(self):
        return self.position_name
    class Meta:
        verbose_name = "position"
        verbose_name_plural = "position"

class Candidates(models.Model):
    candidate = models.ForeignKey(AiUser, on_delete=models.CASCADE)
    postion = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate
    
    class Meta:
        verbose_name = "Candidates"
        verbose_name_plural = "Candidates"

class Vote(models.Model):
    voter = models.ForeignKey(AiUser, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField()

    def __str__(self):
        return self.candidate
    
    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Vote"