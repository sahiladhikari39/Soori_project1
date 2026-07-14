from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        membership = getattr(self.request.user, "membership", None)
        if membership is None:
            return Ticket.objects.none()
        return Ticket.objects.filter(client=membership.client)

    def perform_create(self, serializer):
        membership = self.request.user.membership
        serializer.save(created_by=self.request.user, client=membership.client)