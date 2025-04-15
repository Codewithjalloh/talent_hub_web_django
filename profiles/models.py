from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    USER_TYPES = (
        ('artist', 'Artist'),
        ('actor', 'Actor'),
        ('business', 'Business'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    social_media = models.JSONField(blank=True, null=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class PortfolioItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=200)
    description = models.TextField()
    media_file = models.FileField(upload_to='portfolio/')
    media_type = models.CharField(max_length=20, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.profile.user.username}"
