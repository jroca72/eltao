from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from bonito import views
from bonito.views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name = 'home'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
