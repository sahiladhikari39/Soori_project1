from django.db import models
from django.conf import settings

# Create your models here.
class TicketStatus(models.TextChoices):
    OPEN = 'open', 'Open'
    IN_PROGRESS = 'in_progress', 'In Progress'
    ON_HOLD = 'on_hold', 'On Hold'
    RESOLVED = 'resolved', 'Resolved'
    CLOSED = 'closed', 'Closed'

class TicketPriority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'
    URGENT = 'urgent', 'urgent'


class Ticket(models.Model):
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="tickets")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_created')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets_assigned", limit_choices_to={"role": "support_staff"},)
    title = models.CharField(max_length=255)
    description = models.TextField()
    product_or_service = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=TicketStatus.choices, default=TicketStatus.OPEN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ticket_comments")
    body = models.TextField()
    is_internal_note = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author} on ticket {self.ticket_id}"
    
    