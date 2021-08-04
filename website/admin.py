from django.contrib import admin
from django.contrib.auth.models import User
from .models import Chat, Image, Room,UserDetails,UpdateProfileImage,Comment

admin.site.register(Image)
admin .site .register(UserDetails)
admin .site .register(UpdateProfileImage)
admin.site.register(Comment)
admin.site.register(Room)
admin.site.register(Chat)
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display=["id","content","file"]

class UserDetailsAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","email"]

class UpdateProfileImageAdmin(admin.ModelAdmin): 
    list_display=["id","image","bio"]

class CommentAdmin(admin.ModelAdmin):
    list_display=["id","image","comment","date_created"]

class RoomAdmin(admin.ModelAdmin):
    list_display=["room","username"]

class ChatAdmin(admin.ModelAdmin):
    list_display=["id","message"]
