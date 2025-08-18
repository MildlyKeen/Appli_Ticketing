from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket, Group
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.shortcuts import render
from django.db.models import Count, Q

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'


@login_required
def home(request):
    # On récupère la liste des groupes avec des statistiques sur les tickets associés
    groups = Group.objects.annotate(
        total=Count('tickets'),  # Nombre total de tickets
        open=Count('tickets', filter=Q(tickets__status='open')),  # Nombre de tickets ouverts
        resolved=Count('tickets', filter=Q(tickets__status='closed'))  # Nombre de tickets résolus
    )
    return render(request, 'appli_ticketing/home.html', {'groups': groups})
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

@login_required
def dashboard(request):
    tickets_by_status = Ticket.objects.values('status').annotate(count=Count('id'))
    tickets_by_priority = Ticket.objects.values('priority').annotate(count=Count('id'))
    tickets_by_type = Ticket.objects.values('type').annotate(count=Count('id'))
    
    tickets_by_group = Group.objects.annotate(count=Count('tickets')).values('name', 'count')

    context = {
        'tickets_by_status': list(tickets_by_status),
        'tickets_by_priority': list(tickets_by_priority),
        'tickets_by_type': list(tickets_by_type),
        'tickets_by_group': list(tickets_by_group),
    }
    return render(request, 'appli_ticketing/dashboard.html', context)