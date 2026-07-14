from django.contrib import admin
 
from .models import Client, ClientMembership
 
admin.site.register(Client)
admin.site.register(ClientMembership)