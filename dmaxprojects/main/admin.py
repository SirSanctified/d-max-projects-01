from django.contrib import admin
from .models import Testimonial, Service, Portfolio, Contact

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

@admin.register(Portfolio)
class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ['service', 'is_active']
    list_filter = ('service', 'is_active')
    

@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'location', 'is_active']
    list_filter = ['location', 'is_active']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'received_at']
    list_filter = ['received_at', 'email']
    readonly_fields = ['message', 'first_name', 'last_name', 'email', 'received_at']

