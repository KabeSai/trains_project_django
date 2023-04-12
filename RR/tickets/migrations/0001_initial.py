# Generated by Django 4.1.7 on 2023-04-05 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'additional_service',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('number', models.TextField()),
            ],
            options={
                'db_table': 'passenger',
            },
        ),
        migrations.CreateModel(
            name='RailwayCarriage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.TextField()),
                ('number_of_seats', models.IntegerField()),
                ('seating_plan', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'railway_carriage',
            },
        ),
        migrations.CreateModel(
            name='RailwayStation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'railway_station',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'route',
            },
        ),
        migrations.CreateModel(
            name='RoutePart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('route_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.route')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_route_parts', to='tickets.railwaystation')),
                ('stop_uuid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stop_route_parts', to='tickets.railwaystation')),
            ],
            options={
                'db_table': 'route_part',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField()),
                ('is_booked', models.BooleanField()),
                ('railway_carriage_info_uuid', models.ForeignKey(db_column='railway_carriage_info_uuid', on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.railwaycarriage')),
                ('route_part', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.routepart')),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketToAddService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.additionalservice')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.ticket')),
            ],
            options={
                'db_table': 'ticket_to_add_service',
            },
        ),
        migrations.CreateModel(
            name='HumanTicket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_date', models.DateTimeField(blank=True, null=True)),
                ('passenger_info_id', models.ForeignKey(db_column='passenger_info_uuid', on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.passenger')),
            ],
            options={
                'db_table': 'human_ticket',
            },
        ),
    ]