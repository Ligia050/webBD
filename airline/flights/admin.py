from django.contrib import admin
from .models import Flight, Airport, Passenger, FlightAdmin

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger)

