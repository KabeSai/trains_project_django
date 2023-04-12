from .models import RailwayStation, Passenger, RoutePart, Ticket
from .forms import TicketSearchForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.models import User
from .forms import RegistrationForm
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TicketSerializer
from django.db.models import F


class RoutePartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RoutePart.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_protect
def index(request):
    station = RailwayStation.objects.all()
    find = TicketSearchForm()
    # first_routes = RoutePart.objects.filter(start_id='839b23f0-af64-48c5-8796-ac9cc0b27521',
    #                                       departure__gte='2023-04-06',
    #                                       departure__lte='2023-04-07')
    # second_routes = RoutePart.objects.filter(stop_uuid='39b3e590-c684-4127-8dd1-09cba5926403')
    # my_first_set, my_seocnd_set = set(), set()
    # for element in first_routes:
    #     my_first_set.add(element.route_uuid)
    # for element in second_routes:
    #     my_seocnd_set.add(element.route_uuid)
    # suitable_routes = my_first_set & my_seocnd_set
    # route_parts = [RoutePart.objects.filter(route_uuid=el.id) for el in suitable_routes]
    # start_parts = []
    # for el in route_parts[0]:
    #     part = RoutePart.objects.filter(order=1, route_uuid=el.route_uuid)
    #     if part not in start_parts:
    #         start_parts.append(part)
    # for el in set(start_parts):
    #     print(el)
    return render(request, 'tickets/index.html', {'form' : find, 'station': station})


def scheme(request):
    return render(request, 'tickets/er_scheme.html')


def tickets(request):

    return render(request, 'tickets/tickets.html', {'tickets': 1})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            number = form.cleaned_data.get('number')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=surname,
                email=email,
                password=password
            )
            Passenger.objects.create(
                user=user,
                number=number
            )
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'tickets/register.html', context)



def login_view(request):
    error_msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error_msg = 'Invalid username or password'
    else:
        error_msg = None
    return render(request, 'tickets/login.html', {'error_msg': error_msg})

@decorators.login_required(login_url='login')
def profile(request):
    passenger = Passenger.objects.get(user=request.user)
    return render(request, 'tickets/profile.html', {'passenger':passenger})


def logout_view(request):
    logout(request)
    return redirect('home')


def contacts(request):
    return render(request, 'tickets/contacts.html')