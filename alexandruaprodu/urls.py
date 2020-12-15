
from django.contrib import admin
from django.urls import path, include
from the_artist import urls as the_artist_urls
from the_professional import urls as the_professional_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('the_artist/', include(the_artist_urls)),
    path('the_professional/', include(the_professional_urls)),

]
