from django.urls import path
from the_artist import views as the_artist_views


app_name = 'the_artist'

urlpatterns = [
    path('', the_artist_views.index, name='index'),
]
