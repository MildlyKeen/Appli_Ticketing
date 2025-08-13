from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from .forms import CustomUserCreationForm

@login_required
def home(request):
    # Render the home.html template, which extends base.html and includes navigation
    return render(request, 'appli_ticketing/home.html')

def register(request):
    """
    Handles user registration using a custom form that enforces unique email.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    """
    Display the user's profile and their tickets.
    """
    user_tickets = Ticket.objects.filter(created_by=request.user)
    return render(request, 'appli_ticketing/profile.html', {'user_tickets': user_tickets})