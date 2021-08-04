from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import View
from .models import User,Image,Chat
from .forms import ChatForm, NewUserForm,CustomAuthenticationForm,ImageForm, RoomForm,UserDetailsForm,UpdateProfileImageForm,CommentForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def indexpage(request):
    if request.method=='POST':
        form=CustomAuthenticationForm(request=request,data=request.POST)
        if form. is_valid():
            uname=form.cleaned_data["username"]
            pname=form.cleaned_data["password"]
            user=authenticate(username=uname,password=pname)
            if user is not None:
                login(request,user)
                request.session["msg"]="successful login"
                request.session["login"]=uname
                return redirect("http://localhost:8000/website/profilepage/")

    else:
        form=CustomAuthenticationForm()
    return render(request,"index.html",{'form':form})

@login_required(login_url="http://localhost:8000/website/signinpage")
def homepage(request):
    img=Image.objects.all()
    
    return render(request,"home.html",{'img':img})

def signuppage(request):

     
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect("http://localhost:8000/website/signinpage")
            
            
    
    form = NewUserForm()    
    obj=User.objects.all()
    return render(request,"signup.html",{'form':form})
    
    
def signinpage(request):

    if request.method=='POST':
        form=CustomAuthenticationForm(request=request,data=request.POST)
        if form. is_valid():
            uname=form.cleaned_data["username"]
            pname=form.cleaned_data["password"]
            user=authenticate(username=uname,password=pname)
            if user is not None:
                login(request,user)
                request.session["msg"]="successful login"
                request.session["login"]=uname
                return redirect("http://localhost:8000/website/profilepage/")

    else:
        form=CustomAuthenticationForm()
    return render(request,"signinpage.html",{'form':form})


def signoutpage(request):
    del request.session["msg"]
    del request.session["login"]
    return redirect("http://localhost:8000/website/signinpage")
@csrf_exempt
@login_required(login_url="http://localhost:8000/website/signinpage")
def profilepage(request):
    
    return render(request,"profile.html")


@login_required(login_url="http://localhost:8000/website/signinpage")
def postpage(request):
    
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("http://localhost:8000/website/homepage")
       
    
    form=ImageForm()
    img=Image.objects.all()  
    return render(request,"post.html",{'img':img,'form':form})    


@login_required(login_url="http://localhost:8000/website/signinpage")
def updateprofile(request):
    if request.method == 'POST':
        form1=UpdateProfileImageForm(request.POST,request.FILES,instance=request.user)
        form =UserDetailsForm(request.POST,instance=request.user)
        if form1.is_valid() and form.is_valid():
            form1.save()
            form.save()
    
            
            return redirect("http://localhost:8000/website/profilepage")
    form1=UpdateProfileImageForm(instance=request.user)
    form=UserDetailsForm(instance=request.user)
    return render(request,"updateprofile.html",{'form1':form1,'form':form})


@csrf_exempt
@login_required(login_url="http://localhost:8000/website/signinpage")
def usercomment(request):
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
    form=CommentForm()
    return render(request,"comment.html",{'form':form})


@login_required(login_url="http://localhost:8000/website/signinpage")
def userroom(request):
    if request.method == "POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
    form=RoomForm()
    return render(request,"room.html",{'form':form})

@login_required(login_url="http://localhost:8000/website/signinpage")
def userchat(request):
    if request.method == "POST":
        form=ChatForm(request.POST)
        if form.is_valid():
            form.save()
    form=ChatForm()
    msg=Chat.objects.all()        
    return render(request,"chat.html",{'form':form,'msg':msg})
