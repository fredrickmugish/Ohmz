from django.urls import path
from django.conf.urls.static import static
from .import views
from django.conf import settings

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about_page, name="about"),
    path('services/', views.services_page, name="services"),
    path('contact/', views.contact_page, name="contact"),
    path('contact_data/', views.contact_data, name="contact_data"),
    path('consult', views.consult_page, name="consult"),
    path('cyber', views.cyber_page, name="cyber"),
    path('domain', views.domain_page, name="domain"),
    path('grphics', views.grphics_page, name="graphics"),
    path('hosting', views.hosting_page, name="hosting"),
    path('network', views.network_page, name="network"),
    path('system', views.system_page, name="system"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

