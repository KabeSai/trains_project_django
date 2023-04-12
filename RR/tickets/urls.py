from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Tickets', views.RoutePartViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('scheme', views.scheme, name='scheme'),
    path('tickets', views.tickets, name='tickets'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout/',  views.logout_view, name='logout'),
    path('contacts', views.contacts, name='contacts')
] + router.urls
