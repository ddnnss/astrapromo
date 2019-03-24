from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('seo/', views.seo, name='seo'),
    path('catalog/sozdanie-sajtov-v-chelyabinske/', views.sites, name='sites'),
    path('contacts/', views.contacts, name='contacts'),



]
