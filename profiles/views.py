from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.base import View 
from django.contrib.auth.decorators import login_required
from profiles.forms import UserForm, ProfileForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profiles:view_profile'))
    else:
        form = ProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'page-profile.html', args)