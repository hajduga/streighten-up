from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=("groups"),
        blank=True,
        help_text=("The groups this user belongs to. A user will get all permissions granted to each of their groups."),
        related_name="custom_users",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="custom_users_permissions", 
        related_query_name="user",
    )

    def __str__(self):
        return self.username

class Expert(CustomUser):
    specialization = models.CharField(max_length=255)
    certification = models.FileField(upload_to='certifications/')

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)