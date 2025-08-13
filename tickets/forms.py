from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    """
    Form for regular users to create a ticket.
    Only includes fields they are allowed to set.
    """
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'priority']

class TicketAssignForm(forms.ModelForm):
    """
    Form for staff/admin to assign a ticket and update its status.
    Only staff/admin should use this form.
    """
    class Meta:
        model = Ticket
        fields = ['assigned_to', 'status']