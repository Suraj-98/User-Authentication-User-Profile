from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    id=models.AutoField(primary_key=True)
    content=models.CharField(max_length=80)
    file=models.ImageField(upload_to="myself")

    def __str__(self):
        return self.content

class UserDetails(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(null=True)

class UpdateProfileImage(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to="profilephotos", null=True)
    bio=models.CharField(max_length=250, null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image=models.ForeignKey(Image, on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

class Room(models.Model):
    id=models.AutoField(primary_key=True)
    room=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=100,null=True)

class Chat(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=2000)
