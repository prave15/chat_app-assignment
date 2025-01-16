
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .models import Profile, Message
from django.contrib.auth.models import User
from django.db.models import Q


def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'chat/home.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error_message = "Invalid username or password."
            return render(request, 'chat/login.html', {'error_message': error_message})
    return render(request, 'chat/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    users = User.objects.exclude(username=request.user.username)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'users': users,
    }
    return render(request, 'chat/profile.html', context)


@login_required
def chat_room(request, username):
    other_user = User.objects.get(username=username)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('timestamp')
    
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'messages': messages,
        'users': users,
    })

