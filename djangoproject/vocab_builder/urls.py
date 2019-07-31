from django.urls import path, include
from . import views
from rest_framework import routers
from .api import VocabBuilderViewSet

router = routers.DefaultRouter()
router.register('api/vb', VocabBuilderViewSet, 'vocab_builder-api')

urlpatterns = [
    path('', views.home, name='vocab_builder-home'),
    path('about/', views.about, name='vocab_builder-about'),
    path('', include(router.urls))
]

