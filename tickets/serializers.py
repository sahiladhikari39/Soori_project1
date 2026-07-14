from rest_framework import serializers

from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)
    created_by_username = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'client', 'client_name', 'title', 'description', 'created_by', 'created_by_username', 'created_at']
        read_only_fields = ["created_by", "client"]

    