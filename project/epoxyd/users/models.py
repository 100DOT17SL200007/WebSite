from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile/', default='profile/user.png')
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Message(models.Model):
#     sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
#     recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='messages')
#     name = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=200, blank=True, null=True)
#     subject = models.CharField(max_length=200, blank=True, null=True)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.subject
#
#     class Meta:
#         ordering = ['is_read', '-created']
