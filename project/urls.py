from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from project import settings

urlpatterns = [
    path('', include('main.urls')),
    path('said/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
