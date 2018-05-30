from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.base import View 
from django.contrib.auth.decorators import login_required
from profiles.forms import UserForm, ProfileForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.views import generic
from django.db import transaction

class ProfileListView(generic.ListView):
    queryset = UserProfile.objects.select_related('user')

def get_user_profile(request, username):
    user = User.objects.get(User, username=username)
    return render(request, 'index.html', {"user":user})

def view_profile(request, pk=None):
    if pk:
        user = User.objiects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'index.html', args)

@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('authapp:home')
        else:
            return redirect('authapp:home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'page-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })