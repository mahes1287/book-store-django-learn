from django.urls import path
from .views import HomePageView, AboutPageView, FAQPageView, ContactUsPageView

# app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('faq/', FAQPageView.as_view(), name = 'faq'),
    path('contact-us/', ContactUsPageView.as_view(), name = 'contact_us'),
    # path('search/', SearchView.as_view() , name = 'search_results'),
    ]