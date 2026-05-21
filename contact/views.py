from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from core.models import ContactInfo


def contact_view(request):
    lang = request.GET.get('lang', 'tr')
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            if lang == 'en':
                messages.success(request, 'Your message has been sent successfully.')
            else:
                messages.success(request, 'Mesajınız başarıyla gönderildi.')

            return redirect(f'/contact/?lang={lang}')
        else:
            if lang == 'en':
                messages.error(request, 'An error occurred while sending the message.')
            else:
                messages.error(request, 'Mesaj gönderilirken bir hata oluştu.')
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {
        'form': form,
        'lang': lang,
        'contact_info': contact_info,
    })