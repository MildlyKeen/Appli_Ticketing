from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Ticket
from .forms import TicketForm, TicketAssignForm

def ticket_list(request):
    """
    This view retrieves all Ticket objects from the database and passes
    them to a template for display.
    """
    # Secure Coding Practice:
    # Django's ORM (Object-Relational Mapper) is secure against SQL injection by design.
    # When you use a query like this, Django handles the conversion to SQL safely.

    # The .all() method fetches all objects from the Ticket model.
    tickets = Ticket.objects.all()

    # The context dictionary is used to pass data from the view to the template.
    # The key 'tickets' will be used in the template to access the list of tickets.
    context = {'tickets': tickets}

    # The render() function combines a template with the context dictionary and
    # returns an HttpResponse object, which is sent to the user's browser.
    return render(request, 'tickets/ticket_list.html', context)

@login_required
def ticket_detail(request, pk):
    """
    Display all details for a single ticket.
    pk: primary key of the ticket (from URL)
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_edit(request, pk):
    """
    Allow the user to edit an existing ticket.
    Only the creator or an admin should be able to edit (add logic later).
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets:ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'edit': True})

@login_required
def ticket_delete(request, pk):
    """
    Allow only the creator (or admin) to delete a ticket.
    Shows a confirmation page before deletion.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    # Only allow the creator or superuser to delete
    if request.user != ticket.created_by and not request.user.is_superuser:
        return HttpResponseForbidden("Vous n'avez pas la permission de supprimer ce ticket.")
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

def is_staff(user):
    """
    Helper function to check if the user is staff or superuser.
    Used to restrict assignment functionality.
    """
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_staff)
def ticket_assign(request, pk):
    """
    Allows staff or admin to assign a ticket and update its status.
    Only accessible to staff or superuser.
    """
    ticket = get_object_or_404(Ticket, pk=pk)  # Get the ticket or return 404
    if request.method == 'POST':
        form = TicketAssignForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()  # Save the assignment and status change
            return redirect('ticket_detail', pk=ticket.pk)  # Redirect to ticket detail
    else:
        form = TicketAssignForm(instance=ticket)  # Pre-fill form with current data
    return render(request, 'tickets/ticket_assign.html', {'form': form, 'ticket': ticket})

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('tickets:ticket_list')
        else:
            # Form is invalid, show errors
            return render(request, 'tickets/ticket_form.html', {'form': form, 'edit': False})
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form, 'edit': False})