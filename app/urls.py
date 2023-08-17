from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
  path('characters/', CharacterApiView.as_view(), name='characters'),
  path('characters/<int:id>', CharacterApiView.as_view(), name='characterParam'),
  path('locations/', LocationApiView.as_view(), name='locations'),
  path("locations/<int:id>", LocationApiView.as_view(), name="locationParam"),
  path("episode/", EpisodeApiView.as_view(), name='episodes'),
  path("episode/<int:id>", EpisodeApiView.as_view(), name='episodeParam')
]
