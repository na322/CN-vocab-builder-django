from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vocab_builder-home'),
    path('about/', views.about, name='vocab_builder-about')
]