from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.response import Response
# Create your views here.

class ListingView(viewsets.ModelViewSet):
    """Manually creating view for Listing model."""
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

