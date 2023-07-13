from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



def send_email(request):
    print(request.POST)
    try:
        to_email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(

            subject='Bu xabar test uchun ishlatildi',

            message=message,

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[to_email],
        )
    except Exception as e:
        return HttpResponse('<h1>Emailiz xato kiritildi!!!</h1>')


    return render(request=request, template_name='index.html')
