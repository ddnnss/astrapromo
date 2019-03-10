from django.shortcuts import render
from django.http import JsonResponse
from customUser.models import callBack

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
        return JsonResponse(return_dict)

