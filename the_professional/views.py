from django.shortcuts import render
from .models import BackEndSkills, SoftSkills, Services, Projects, Counter, IntroductionCv
from django.core.mail import send_mail

email_rec = ['alexandruaprodu.prof@gmail.com']


def index(request):
    context = {'BackEndSkills': BackEndSkills.objects.all(), 'SoftSkills': SoftSkills.objects.all(),
               'Services': Services.objects.all(), 'Projects': Projects.objects.all(), 'Counter': Counter.objects.all(),
               'IntroductionCv': IntroductionCv.objects.latest('id'), 'title': 'Alexandru Aprodu'}
    return render(request, 'the_professional/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Informatii despre : ' + name,  # subiect
            message,  # mesaj
            email,  # from email
            email_rec,  # to email
        )
        return render(request, 'the_professional/contact.html', {'name': name})
    else:
        return render(request, 'the_professional/contact.html', {'title': 'Contact Form'})
