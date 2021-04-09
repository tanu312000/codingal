from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pagesapp import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pagesapp/', include('pagesapp.urls')),


    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)