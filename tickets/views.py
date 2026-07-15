from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_soori_admin:
            return Ticket.objects.all()
        if user.client_id is None:
            # Shouldn't happen given the model's CheckConstraint, but
            # never fall back to "show everything" if it somehow does.
            return Ticket.objects.none()
        return Ticket.objects.filter(client_id=user.client_id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, client_id=self.request.user.client_id)
