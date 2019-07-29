from django.urls import path, include
from . import views
from rest_framework import routers
from .api import VocabBuilderViewSet

# router = routers.DefaultRouter()
# router.register('vocab_builder', views.api_build, 'vocab_builder-api')

urlpatterns = [
    path('', views.home, name='vocab_builder-home'),
    path('about/', views.about, name='vocab_builder-about'),
    path('api/build', views.api_build, name='api-build'),
    path('api/history', views.api_history, name='api-history'),
    path('api/vocab', views.api_vocab, name='api-vocab')
]

