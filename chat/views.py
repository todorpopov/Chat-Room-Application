from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib import messages


def frontpage(request):
    return render(request, 'chat/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
        else:
            messages.error(request, 'Sign up failed! Please enter valid details.')
    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'forms': form})