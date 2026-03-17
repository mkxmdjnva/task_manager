from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserPrivacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    show_online = models.BooleanField(default=False)
    allow_search = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} maxfiylik sozlamalari"

class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('in  progress', 'Jarayonda'),
        ('done', 'Bajarildi'),
    )
    PRIORITY_CHOICES = (
        ('low', 'Past'),
        ('normal', 'oddiy'),
        ('high', 'Baland'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    deadline = models.DateTimeField(auto_created=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

class Category(models.Model):
    name = models.CharField(max_length=100)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)