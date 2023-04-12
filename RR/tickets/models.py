from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class NameMixin(models.Model):
    name = models.TextField()

    class Meta:
        abstract = True
        
        
class PriceMixin(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class AdditionalService(UUIDMixin, PriceMixin, NameMixin):
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'additional_service'

    def __str__(self) -> str:
        return self.name

class HumanTicket(UUIDMixin, PriceMixin):
    passenger_info_id = models.ForeignKey('Passenger', models.DO_NOTHING, db_column='passenger_info_uuid')
    booking_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'human_ticket'


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    number = models.TextField()

    class Meta:
        db_table = 'passenger'

    def __str__(self) -> str:
        return f"{self.user.username} {self.user.last_name}"


class RailwayCarriage(UUIDMixin):
    type = models.TextField()
    number_of_seats = models.IntegerField()
    seating_plan = models.TextField(blank=True, null=True)  

    class Meta:
        db_table = 'railway_carriage'
        
    def __str__(self) -> str:
        return self.type


class RailwayStation(UUIDMixin, NameMixin):
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  

    class Meta:
        db_table = 'railway_station'
        
    def __str__(self) -> str:
        return self.name


class Route(UUIDMixin):

    class Meta:
        db_table = 'route'


class RoutePart(UUIDMixin):
    start = models.ForeignKey(RailwayStation, on_delete=models.CASCADE, related_name='start_route_parts')
    stop_uuid = models.ForeignKey(RailwayStation, on_delete=models.CASCADE, null=True, blank=True, related_name='stop_route_parts')
    route_uuid = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    order = models.IntegerField()


    class Meta:
        db_table = 'route_part'

    def __eq__(self, other: object) -> bool:
        return self.id == other.id


class Ticket(UUIDMixin):
    route_part = models.ForeignKey(RoutePart, models.DO_NOTHING)
    railway_carriage_info_uuid = models.ForeignKey(RailwayCarriage, models.DO_NOTHING, db_column='railway_carriage_info_uuid')
    seat_number = models.IntegerField()
    is_booked = models.BooleanField()

    class Meta:
        db_table = 'ticket'


class TicketToAddService(UUIDMixin):
    add = models.ForeignKey(AdditionalService, models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, models.DO_NOTHING)

    class Meta:
        db_table = 'ticket_to_add_service'



