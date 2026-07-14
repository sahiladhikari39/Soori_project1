from django.db import models
from django.conf import settings


class Client(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ClientMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="membership")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return f"{self.user.username} @ {self.client.name}"
    