from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuItems, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer