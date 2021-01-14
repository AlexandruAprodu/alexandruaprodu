from django.urls import path
from the_professional import views as the_professional_views


app_name = 'the_professional'

urlpatterns = [
    path('', the_professional_views.index, name='index'),
    path('contact', the_professional_views.contact, name='contact'),
]
