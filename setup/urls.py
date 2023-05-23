from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('manager', include('manager.urls')),
    path('logout/', RedirectView.as_view(url = '/admin/logout/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
