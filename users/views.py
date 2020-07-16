from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


# this view will be shown when any one visit our website address e.g domain.com/register
# URL Of this view is mapped inside the urls.py of this folder

def registration(request):
    """view for our registration page."""

    if request.method == "POST":  # checking if the request method is POST or not.
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # this will show the success messages if user registred successfully
            messages.success(
                request, f'Your Account has been created! Login To Proceed further')
            return redirect('/user/login/')
    else:
        # If the request is other than POST request then this will show a blank form.
        form = UserRegistrationForm()
    return render(request, 'register.html', context={'form': form})
