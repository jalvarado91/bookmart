from django.shortcuts import render
from django.core.urlresolvers import reverse


def rendermessage(request, title, header, message, url, page_name):
    return render(request, 'user_message.html', {
        'page_title': title,
        'page_header': header,
        'page_message': message,
        'url_to_redirect': url,
        'returning_page_name': page_name
    })


def renderconfirmation(request, form, title, question_header, question_body):
    return render(request, 'confirmation.html', {
        'form': form,
        'page_title': title,
        'question_header': question_header,
        'question_body': question_body
    })


def render_access_denied_message(request):
    return render(request, 'Error', 'Access denied',
                  'Contact the administrator', reverse('home'), 'home page')
