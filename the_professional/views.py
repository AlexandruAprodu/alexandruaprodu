from django.shortcuts import render


def index(request):
    return render(request, 'the_professional/index.html')
