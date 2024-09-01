from django.contrib import admin

# Register your models here.
from .models import MenuItems, Booking

admin.site.register(MenuItems)
admin.site.register(Booking)
