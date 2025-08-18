from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.db.models import Count
from .models import Ticket, Group
from .forms import TicketForm, TicketAssignForm
from .forms_group import GroupForm

def is_staff_user(user):
    return user.is_staff or user.is_superuser

@login_required
def ticket_list(request):
    group_name = request.GET.get('group')
    tickets = Ticket.objects.all()
    if group_name:
        tickets = tickets.filter(group__name__iexact=group_name)
    context = {
        'tickets': tickets,
        'filtered_group': group_name,
        'all_groups': Group.objects.annotate(
            total=Count('tickets'),
            open=Count('tickets', filter=models.Q(tickets__status='open')),
            resolved=Count('tickets', filter=models.Q(tickets__status='closed'))
        )
    }
    return render(request, 'tickets/ticket_list.html', context)

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, user=request.user)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('tickets:ticket_list')
    else:
        form = TicketForm(user=request.user)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'edit': False})

@login_required
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.user != ticket.created_by and not request.user.is_superuser:
        return HttpResponseForbidden("Permission refusée.")
    form = TicketForm(request.POST or None, instance=ticket, user=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tickets:ticket_detail', pk=ticket.pk)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'edit': True})

@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.user != ticket.created_by and not request.user.is_superuser:
        return HttpResponseForbidden("Permission refusée.")
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets:ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

@login_required
@user_passes_test(is_staff_user)
def ticket_assign(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketAssignForm(request.POST or None, instance=ticket)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tickets:ticket_detail', pk=ticket.pk)
    return render(request, 'tickets/ticket_assign.html', {'form': form, 'ticket': ticket})

@login_required
@user_passes_test(is_staff_user)
def group_create(request):
    form = GroupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tickets:ticket_create')
    return render(request, 'tickets/group_form.html', {'form': form})

@login_required
def dashboard(request):
    tickets_by_status = Ticket.objects.values('status').annotate(count=Count('id'))
    tickets_by_priority = Ticket.objects.values('priority').annotate(count=Count('id'))
    tickets_by_type = Ticket.objects.values('type').annotate(count=Count('id'))
    group_stats = Group.objects.annotate(
        total=Count('tickets'),
        open=Count('tickets', filter=models.Q(tickets__status='open')),
        resolved=Count('tickets', filter=models.Q(tickets__status='closed'))
    )
    context = {
        'tickets_by_status': list(tickets_by_status),
        'tickets_by_priority': list(tickets_by_priority),
        'tickets_by_type': list(tickets_by_type),
        'group_stats': group_stats,
    }
    return render(request, 'appli_ticketing/dashboard.html', context)
