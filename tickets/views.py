from django.shortcuts import render
from .models import Ticket

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
