from django.shortcuts import render

from .models import UserMessage


def getform(request):
    all_message = UserMessage.objects.filter(name='Cash')

    for msg in all_message:
        print(msg.name + ' : ' + msg.message)

    return render(request, 'message/message_form.html')
