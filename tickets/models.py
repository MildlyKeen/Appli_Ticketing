from django.db import models

class Ticket(models.Model):
    # The title of the ticket. CharField is for short strings.
    title = models.CharField(max_length=200)

    # A detailed description of the issue. TextField is for longer text.
    description = models.TextField()

    # Automatically records the date and time the ticket was created.
    # The auto_now_add=True argument means this field is set automatically
    # the first time the object is saved to the database.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        This method defines the string representation of a Ticket object.
        It's helpful for displaying objects in the Django admin.
        """
        return self.title