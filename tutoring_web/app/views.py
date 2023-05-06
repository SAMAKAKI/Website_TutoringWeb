from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import *

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

class OpinionsView(View):
    def get(self, request, *args, **kwargs):
        opinions = Opinion.objects.all()
        if opinions:
            all_stars = 0
            for opinion in opinions:
                all_stars += opinion.mark
        
            website_mark = all_stars / len(opinions)
        else:
            website_mark = 0
        return render(request, 'app/opinions.html', locals())
    
    def post(self, request, *args, **kwargs):
        error = ''
        if request.POST.get('star'):
            if request.POST.get('text-opinion'):
                new_opinion = Opinion(user=request.user, mark=request.POST.get('star'), opinion=request.POST.get('text-opinion'))
                new_opinion.save()
                return redirect('opinions')
            else:
                error = 'Musisz wpisać text'
        else:
            error = 'Musisz wybrać gwiazdkę'
        return render(request, 'app/opinions.html', locals())