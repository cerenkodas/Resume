from django.shortcuts import render
from .models import (
    HomeHero,
    HomeFloatingCard,
    SocialMedia,
    SiteSetting,
    AboutInfo,
    AboutCard,
    ResumeEducation,
    ResumeExperience,
    Certificate,
    ProfessionalSkill,
    SkillGroup,
    Project,
)


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


def about(request):
    lang = get_lang(request)

    about_info = AboutInfo.objects.filter(is_active=True).first()
    personal_cards = AboutCard.objects.filter(is_active=True, card_type='personal')
    interest_cards = AboutCard.objects.filter(is_active=True, card_type='interest')

    return render(request, 'about.html', {
        'lang': lang,
        'about_info': about_info,
        'personal_cards': personal_cards,
        'interest_cards': interest_cards,
    })


def resume(request):
    lang = get_lang(request)

    educations = ResumeEducation.objects.filter(is_active=True)
    experiences = ResumeExperience.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    professional_skills = ProfessionalSkill.objects.filter(is_active=True)

    return render(request, 'resume.html', {
        'lang': lang,
        'educations': educations,
        'experiences': experiences,
        'certificates': certificates,
        'professional_skills': professional_skills,
    })

def skills(request):
    lang = get_lang(request)

    skill_groups = SkillGroup.objects.filter(is_active=True)

    return render(request, 'skills.html', {
        'lang': lang,
        'skill_groups': skill_groups,
    })


def portfolio(request):
    lang = get_lang(request)

    projects = Project.objects.filter(is_active=True)

    return render(request, 'projects.html', {
        'lang': lang,
        'projects': projects,
    })


def contact(request):
    return render(request, 'contact.html', {'lang': get_lang(request)})