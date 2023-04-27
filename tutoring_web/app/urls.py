from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('additional-info/', AdditionalInfoView.as_view(), name='additional-info'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('contact-me/', ContactMeView.as_view(), name='contact-me'),
]
