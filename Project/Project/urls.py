from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace="Home")),
    path('profile/', include('Profile.urls', namespace="Profile")),
    path('notes/', include('Notes.urls', namespace="Notes")),
    path('save/', include('DefinitionsAndExplanations.urls', namespace='Definition')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
