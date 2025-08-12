from django.urls import path
from . import views

# This list contains all the URL patterns for the 'tickets' app.
# The 'app_name' is used for namespacing and is a secure practice
# to prevent URL name conflicts with other apps in the project.
app_name = 'tickets'
urlpatterns = [
    # The `path()` function links a URL to a view.
    # The first argument, '', means this is the root URL for the app (e.g., /tickets/).
    # The second argument, `views.ticket_list`, points to the function we wrote.
    # The third argument, `name='ticket_list'`, gives this URL a name for easy reference in templates.
    path('', views.ticket_list, name='ticket_list'),
]
