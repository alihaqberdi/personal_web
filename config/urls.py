from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.settings import DEBUG
from django.conf.urls import handler404, handler500
import environ

env = environ.Env()
environ.Env.read_env()

handler404 = 'portfolio.views.error_404'
handler500 = 'portfolio.views.error_500'
urlpatterns = [
    path(env('ADMIN'), admin.site.urls),
    path('', include('portfolio.urls')),
]

admin.site.site_header = 'Administration'
admin.site.index_title = 'Alijon'
admin.site.site_title = 'Alijon Adminsitration'

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
