from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Service, ContactMessage
from .forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServicesView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'
