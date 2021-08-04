from django import forms
from .models import Chat, Image, Room,UserDetails,UpdateProfileImage,Comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class CustomAuthenticationForm(AuthenticationForm):
	class Meta:
		fields=("username","password")

    



class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields=('file','content') 



class UserDetailsForm(forms.ModelForm):
	class Meta:
		model=UserDetails
		fields="__all__"


class UpdateProfileImageForm(forms.ModelForm):
	class Meta:
		model=UpdateProfileImage
		fields="__all__"

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=("id","user","comment")

class RoomForm(forms.ModelForm):
	class Meta:
		model=Room
		fields="__all__"

class ChatForm(forms.ModelForm):
	class Meta:
		model=Chat
		fields="__all__"
