from django.shortcuts import render
from .models import BackEndSkills, SoftSkills, Services, Projects, Counter, IntroductionCv


def index(request):
    context = {'BackEndSkills': BackEndSkills.objects.all(), 'SoftSkills': SoftSkills.objects.all(),
               'Services':Services.objects.all(), 'Projects': Projects.objects.all(), 'Counter': Counter.objects.all(),
               'IntroductionCv': IntroductionCv.objects.latest('id'), 'title': 'Alexandru Aprodu'}
    return render(request, 'the_professional/index.html', context)
