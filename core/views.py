from django.shortcuts import render


def get_lang(request):
    return request.GET.get('lang', 'tr')


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