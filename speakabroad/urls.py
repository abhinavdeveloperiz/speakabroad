
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('Study_in_india/', views.Study_in_india, name='Study_in_india'),
    path('Study_in_abroad/', views.Study_in_abroad, name='Study_in_abroad'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
