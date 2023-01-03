from django.shortcuts import render, redirect
from .models import Testimonial, Portfolio
from .forms import ContactForm

def home(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'index.html', context)

def services(request):
    context = {}
    return render(request, 'services.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def gallery(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'gallery.html', context)