from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', locals())

class AdditionalInfoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/additional-info.html', locals())

class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about-me.html', locals())

class ContactMeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact-me.html', locals())