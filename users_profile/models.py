from django.db import models
from django.contrib.auth.models import User
from Posts.models import Post




class Saved(models.Model):
    title=models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to="profile_pciture", null=True, default="default.jpg")
    first_name=models.CharField(max_length=50)
    last_name=models.CharField( max_length=50)
    bio=models.CharField( max_length=150)
    location=models.CharField( max_length=50)
    site_url=models.URLField( max_length=200)
    hightlights=models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.user} : {self.first_name}"

