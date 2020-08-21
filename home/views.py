from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from itertools import chain


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FAQPageView(TemplateView):
    template_name = 'faq.html'

class ContactUsPageView(TemplateView):
    template_name = 'Contact-us.html'
