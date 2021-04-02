from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Notes.models import Notes

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('Profile:Login')
        else:
            return redirect('Profile:Retry')
    
    return render(request, 'Profile/register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('Profile:Profile')
    return render(request, 'Profile/login.html')

@login_required
def User_Profile(request):
    user = request.user

    saved_notes = user.profile.copied_notes.all()

    notes = Notes.objects.filter(user=user)

    definitions = user.profile.saved_definitions.all()

    explanations = user.profile.saved_explanations.all()

    videos = user.profile.saved_videos.all()

    context = {
        "user":user,
        "saved_notes":saved_notes,
        "notes":notes,
        "definitions":definitions,
        "explanations":explanations,
        "videos":videos,
        }

    
    return render(request, "Profile/Profile.html",context)


def View_Profile(request, slug):
    profile = Profile.objects.get(slug=slug)

    definitions = profile.saved_definitions.all()
    explanations = profile.saved_explanations.all()
    notes = Notes.objects.filter(user=profile.user,status="Pu")

    context = {
        "profile":profile,
        "definitions":definitions,
        "explanations":explanations,
        "notes":notes,
        }

    return render(request, "Profile/ViewProfile.html",context)

def Retry_Login(request):
    return render(request,"Profile/Retry_Login.html")
