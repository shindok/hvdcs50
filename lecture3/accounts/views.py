from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login


# Create your views here.
@login_required
def profile_redirect(request):
    return redirect("accounts:profile", username=request.user.username)
    # return redirect('profile', username=request.user.username)

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, "accounts/profile.html", {"user": user})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            #Log the user in
            backend = "accounts.backend.CustomAuthBackend"
            login(request, user, backend=backend)

            return redirect(reverse("accounts:profile", kwargs={"username": username}))
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})