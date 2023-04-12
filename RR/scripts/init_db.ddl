CREATE EXTENSION "uuid-ossp";

DROP TABLE IF EXISTS ticket_to_add_service, additional_service, ticket, route_part, route, railway_station, railway_carriage, passenger, human_ticket CASCADE;

CREATE TABLE passenger (
    id int PRIMARY KEY  GENERATED ALWAYS AS IDENTITY,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT,
    number TEXT NOT NULL,
    password TEXT NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE DEFAULT NULL
);

CREATE TABLE railway_carriage (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type TEXT NOT NULL,
    number_of_seats INT NOT NULL,
    seating_plan JSON
);

CREATE TABLE railway_station (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    description TEXT,
    location POINT
);

CREATE TABLE route (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
);

CREATE TABLE route_part (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    start_id UUID NOT NULL REFERENCES railway_station(id),
    stop_uuid UUID REFERENCES railway_station(id),
    route_uuid UUID REFERENCES route(id),
    departure TIMESTAMP WITH TIME ZONE NOT NULL,
    arrival TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE TABLE additional_service (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    description TEXT
);

CREATE TABLE ticket (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_part_id UUID NOT NULL REFERENCES route_part(id),
    railway_carriage_info_uuid UUID NOT NULL REFERENCES railway_carriage(id),
    seat_number INT NOT NULL,
    is_booked BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE ticket_to_add_service (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    add_id UUID NOT NULL REFERENCES additional_service(id),
    ticket_id UUID NOT NULL REFERENCES ticket(id)
);

CREATE TABLE human_ticket(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),  
    passenger_info_uuid int NOT NULL REFERENCES passenger(id),
    booking_date TIMESTAMP WITH TIME ZONE,
    price NUMERIC NOT NULL
)