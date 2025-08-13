from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    """
    Form for regular users to create a ticket.
    Only includes fields they are allowed to set.
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if not user or not (user.is_staff or user.is_superuser):
            self.fields.pop('group')
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'priority', 'group']

class TicketAssignForm(forms.ModelForm):
    """
    Form for staff/admin to assign a ticket and update its status.
    Only staff/admin should use this form.
    """
    class Meta:
        model = Ticket
        fields = ['assigned_to', 'status', 'group']