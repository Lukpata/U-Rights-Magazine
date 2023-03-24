from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('noise/',include('noise.urls')),
    path('bookstore/',include('bookstore.urls')),
    path('tinymce/',include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)