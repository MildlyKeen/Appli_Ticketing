from django.contrib import admin

# Import the Ticket model from the current directory's models.py file.
from .models import Ticket, Group

# Register your model with the admin site.
# This makes the Ticket model visible and manageable in the Django admin.
admin.site.register(Ticket)
admin.site.register(Group)  