from rest_framework import serializers

from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'client', 'client_name', 'title', 'description', 'created_at']

    