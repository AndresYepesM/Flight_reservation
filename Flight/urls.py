from django.contrib import admin
from django.urls import path, include
from flightApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Flights', views.FlightViewSet)
router.register('Passengers', views.PassengerViewSet)
router.register('Reservation', views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/find_flights/', views.find_flight),

    path('api/save_reservation/', views.save_reservation),
]
