from django.shortcuts import render
from .models import HomeHero, HomeFloatingCard, SocialMedia, SiteSetting


def get_lang(request):
    return request.GET.get('lang', 'tr')


def index(request):
    lang = get_lang(request)

    home_hero = HomeHero.objects.filter(is_active=True).first()
    floating_cards = HomeFloatingCard.objects.filter(is_active=True)
    social_medias = SocialMedia.objects.filter(is_active=True)
    site_setting = SiteSetting.objects.filter(is_active=True).first()

    return render(request, 'index.html', {
        'lang': lang,
        'home_hero': home_hero,
        'floating_cards': floating_cards,
        'social_medias': social_medias,
        'site_setting': site_setting,
    })

def index(request):
    return render(request, 'index.html', {'lang': get_lang(request)})


def about(request):
    return render(request, 'about.html', {'lang': get_lang(request)})


def resume(request):
    return render(request, 'resume.html', {'lang': get_lang(request)})


def skills(request):
    return render(request, 'skills.html', {'lang': get_lang(request)})


def portfolio(request):
    return render(request, 'projects.html', {'lang': get_lang(request)})


def contact(request):
    return render(request, 'contact.html', {'lang': get_lang(request)})