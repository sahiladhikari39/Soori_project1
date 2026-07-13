from django.db import models

# Create your models here.
class Ticket(models.Model):
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="tickets")
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title