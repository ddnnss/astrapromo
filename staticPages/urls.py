from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('seo/', views.seo, name='seo'),
    path('services/seo/', views.seo, name='seo'),
    path('portfolio/', views.showcase, name='showcase'),
    path('sites/', views.sites, name='sites'),
    path('services/sites/', views.sites, name='sites'),
    path('contacts/', views.contacts, name='contacts'),
    path('context/', views.context, name='context'),
    path('services/context/', views.context, name='context'),
    path('target/', views.target, name='target'),
    path('services/target/', views.target, name='target'),
    path('caseinfo/', views.caseinfo, name='caseinfo'),
    path('services/', views.services, name='services'),
    path('robots.txt', views.robots, name='robots'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('index.html', views.index, name='index.html'),
    path('index.php', views.index, name='index.php'),



]
