from django.shortcuts import render, redirect
from .forms import *
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    allUsers = User.objects.all() # selct * from movie
    
    context = {
        "users": allUsers,
    }

    return render(request, 'main/index.html', context)

# registrations
def register(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    #if they are not logged in
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST or None)
            # check if the form is valid
            if form.is_valid():
                user = form.save()

                # get the raw password
                raw_password = form.cleaned_data.get('password1')

                # authenticate the user
                user = authenticate (username=user.username, password=raw_password)

                # login the user
                login(request, user)
                
                return redirect("main:home")
        else:
            form = RegistrationForm()
        return render(request, "accounts/register.html", {"form": form})

# login
def login_user(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            # check the ecredentials
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main:home")
                else:
                    return render(request, 'accounts/login.html', {"error": "Your account has been disabled."})
            else:
                return render(request, 'accounts/login.html', {"error": "Invalid Username or Password. Try Again."})
        return render(request, 'accounts/login.html')

# logout user
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts:login")
    else:
        return redirect("accounts:login")

#edit profile
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('main:home')

    def get_object(self):
        return self.request.user

# edit password
class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('main:home')

@login_required
def delete_profile(request):
  if request.method == 'POST':
    Profile.objects.get(user=request.user).delete()
    success_url = reverse_lazy('main:home')
  else:
    return redirect("accounts:login")


