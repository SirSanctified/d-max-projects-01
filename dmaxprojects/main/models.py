from django.db import models
from django.utils import timezone

class Testimonial(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='testimonials/', null=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    testimonial_body = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.full_name}, {self.location}'

class Service(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image_before = models.ImageField(upload_to='portfolios/', null=True)
    image_after = models.ImageField(upload_to='portfolios/', null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.service.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    received_at = models.DateTimeField(default=timezone.now)