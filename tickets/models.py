from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    # Choices for ticket status
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    # Choices for ticket priority
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=200)  # Title of the ticket
    description = models.TextField()          # Detailed description
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'                        # Default status is 'open'
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'                      # Default priority is 'medium'
    )
    created_by = models.ForeignKey(
        User, related_name='tickets_created', on_delete=models.CASCADE
    )                                         # User who created the ticket
    assigned_to = models.ForeignKey(
        User, related_name='tickets_assigned', on_delete=models.SET_NULL,
        null=True, blank=True,
        help_text="The staff member assigned to this ticket"
    )                                         # Staff member assigned to the ticket
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Last update timestamp
    closed_at = models.DateTimeField(null=True, blank=True)  # When ticket was closed

    def __str__(self):
        return self.title  # String representation for admin and debugging