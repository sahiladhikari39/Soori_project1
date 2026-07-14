from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerializer

# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        qs = Ticket.objects.all()
        client_id = self.request.query_params.get("client")

        if client_id:
            qs = qs.filter(client_id=client_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)