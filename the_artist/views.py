from django.shortcuts import render
from .models import Prime, ImagesPrime, AudioMixes, FacebookLive, Biography
from django.core.mail import send_mail

email_rec = ['alexandruaprodu.prof@gmail.com']


def index(request):

    last_three = ImagesPrime.objects.order_by('-id')[:3][::-1]
    first_image = last_three[0]
    second_image = last_three[1]
    third_image = last_three[2]
    context = {'prime': Prime.objects.all(), 'images_prime': ImagesPrime.objects.all(),
               'audiomixes': AudioMixes.objects.all(), 'facebook_live': FacebookLive.objects.all(),
               'first_image': first_image, 'second_image': second_image, 'third_image': third_image,
               'biography': Biography.objects.all(), 'title': 'Alexandru Aprodu'}
    return render(request, 'the_artist/index.html', context)


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
        return render(request, 'the_artist/contact.html', {'name': name})
    else:
        return render(request, 'the_artist/contact.html', {'title': 'Contact Form'})