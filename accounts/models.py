from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.

from .managers import UserManager

class Role(models.TextChoices):
    SOORI_ADMIN = "soori_admin", "Soori Admin"
    CLIENT_ADMIN = "client_admin", "Client Admin"
    SUPPORT_STAFF = "support_staff", "Support Staff"
    SUB_CLIENT = "sub_client", "Sub-Client"


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices)   
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, null=True, blank=True, related_name="users")
    objects = UserManager()

    class Meta:
        constraints = [models.CheckConstraint(condition=(models.Q(role=Role.SOORI_ADMIN, client__isnull=True) | (~models.Q(role=Role.SOORI_ADMIN) & models.Q(client__isnull=False))), name="soori_admin_has_no_client_others_require_client",)]

    def clean(self):
        super().clean()
        if self.role == Role.SOORI_ADMIN and self.client_id is not None:
            raise ValidationError("Soori Admin users must not belong to a Client.")
        if self.role != Role.SOORI_ADMIN and self.client_id is None:
            raise ValidationError(f"{self.get_role_display()} users must belong to a Client.")

    @property
    def is_soori_admin(self):
        return self.role == Role.SOORI_ADMIN