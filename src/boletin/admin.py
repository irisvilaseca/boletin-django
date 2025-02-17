from django.contrib import admin

# Register your models here.
from .models import Registered
from .forms import RegModelForm

class AdminRegistered(admin.ModelAdmin):
    # Display columns in the admin panel
    list_display = ["email", "name", "timestamp"]
    # Handles data validation in the admin panel
    forms = RegModelForm
    # Makes the "name" field a clickable link to edit the record
    list_display_links = ["name"]
    # Adds a filter in the admin panel based on date and time
    list_filter = ["timestamp"]
    # Allows editing the "name" field directly from the list view
    list_editable = ["name"]
    # Adds a search bar for email or name
    search_fields = ["email", "name"]
    
    # Defines the model associated with this admin configuration
    class Meta:
        model = Registered

admin.site.register(Registered)
