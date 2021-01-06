from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from the_artist import urls as the_artist_urls
from home import urls as home_urls
# from the_professional import urls as the_professional_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('the_artist/', include(the_artist_urls)),
    path('', include(home_urls)),
    # path('the_professional/', include(the_professional_urls)),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
