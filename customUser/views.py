from django.shortcuts import render
from django.http import JsonResponse
from customUser.models import callBack, quizForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def callback(request):
    if request.POST:
        return_dict = {}
        client_name = request.POST.get('client_name')
        client_phone = request.POST.get('client_phone')
        client_email = request.POST.get('client_email')
        if client_email:
            callBack.objects.create(clientEmail=client_email,
                                    clientName=client_name,
                                    clientPhone=client_phone)
        else:
            callBack.objects.create(clientName=client_name,
                                    clientPhone=client_phone)
        return_dict['result'] = 'ok'
        msg_html = render_to_string('email/callback.html')
        send_mail('Заполнена форма обратной связи', None, 'asupport@astrapromo.ru', ['igor@astrapromo.ru'],
                  fail_silently=False, html_message=msg_html)
        return JsonResponse(return_dict)


def quiz(request):
    if request.POST:
        return_dict = {}
        step0 = request.POST.get('step0')
        step1 = request.POST.get('step1')
        step2 = request.POST.get('step2')
        step3 = request.POST.get('step3')
        step4 = request.POST.get('step4')
        quizForm.objects.create(step0=step0,
                                step1=step1,
                                step2=step2,
                                step3=step3,
                                step4=step4)
        return_dict['result'] = 'ok'
        msg_html = render_to_string('email/quiz.html')
        send_mail('Заполнен квиз', None, 'asupport@astrapromo.ru', ['igor@astrapromo.ru'],
                  fail_silently=False, html_message=msg_html)
        return JsonResponse(return_dict)